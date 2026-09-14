import pandas as pd
from sqlalchemy import create_engine, text
import logging
from config import DB_CONNECTION_STRING
import os

os.makedirs('logs', exist_ok=True)
logging.basicConfig(filename='logs/etl_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def transform_and_load_clean():
    engine = create_engine(DB_CONNECTION_STRING)
    
    try:
        df = pd.read_sql("SELECT * FROM raw_currency_rates", engine)
        if df.empty:
            print("Transform qilish uchun raw table'da ma'lumot topilmadi.")
            return
            
        df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y').dt.date
        df['rate_per_unit'] = df['rate'] / df['nominal']
        
        def get_direction(diff_val):
            if diff_val > 0: return 'Increased'
            elif diff_val < 0: return 'Decreased'
            else: return 'No Change'
            
        df['change_direction'] = df['diff'].apply(get_direction)
        df['is_appreciated'] = df['diff'] > 0
        df['is_depreciated'] = df['diff'] < 0
        
        clean_df = df[['ccy', 'ccy_nm_en', 'nominal', 'rate', 'diff', 'date', 'rate_per_unit', 'change_direction', 'is_appreciated', 'is_depreciated']].copy()
        clean_df.columns = ['currency_code', 'currency_name', 'nominal', 'rate_uzs', 'diff_uzs', 'rate_date', 'rate_per_unit', 'change_direction', 'is_appreciated', 'is_depreciated']
        
        clean_df = clean_df.dropna(subset=['currency_code', 'rate_date'])
        clean_df = clean_df.drop_duplicates(subset=['currency_code', 'rate_date'], keep='last')
        
        
        with engine.begin() as conn:
            conn.execute(text("DELETE FROM clean_currency_rates"))
            
        clean_df.to_sql('clean_currency_rates', engine, if_exists='append', index=False)
        print("Tozalangan ma'lumotlar clean jadvalga yuklandi.")
        
    except Exception as e:
        logging.error(f"Transform xatoligi: {e}")
        print(f"Xatolik yuz berdi: {e}") 

if __name__ == "__main__":
    transform_and_load_clean()