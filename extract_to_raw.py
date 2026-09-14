import requests
import json
import pandas as pd
import logging
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from config import DB_CONNECTION_STRING

logging.basicConfig(filename='logs/etl_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def extract_cbu_data(days_back=5):
    engine = create_engine(DB_CONNECTION_STRING)
    
    for i in range(days_back, -1, -1):
        target_date = datetime.now() - timedelta(days=i)
        date_str = target_date.strftime('%Y-%m-%d')
        url = f"https://cbu.uz/uz/arkhiv-kursov-valyut/json/all/{date_str}/"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            raw_records = []
            for item in data:
                record = {
                    'ccy': item.get('Ccy'),
                    'ccy_nm_uz': item.get('CcyNm_UZ'),
                    'ccy_nm_ru': item.get('CcyNm_RU'),
                    'ccy_nm_en': item.get('CcyNm_EN'),
                    'nominal': int(item.get('Nominal', 1)),
                    'rate': float(item.get('Rate', 0)),
                    'diff': float(item.get('Diff', 0)) if item.get('Diff') else 0.0,
                    'date': item.get('Date'),
                    'source_system': 'CBU_JSON',
                    'raw_json': json.dumps(item)
                }
                raw_records.append(record)
                
            if raw_records:
                df_raw = pd.DataFrame(raw_records)
                df_raw.to_sql('raw_currency_rates', engine, if_exists='append', index=False)
                print(f"{date_str}: Raw jadvalga yuklandi.")
                
        except Exception as e:
            logging.error(f"Xatolik {date_str}: {e}")

if __name__ == "__main__":
    extract_cbu_data(5)