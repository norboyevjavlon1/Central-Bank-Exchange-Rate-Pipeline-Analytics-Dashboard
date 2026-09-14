from extract_to_raw import extract_cbu_data
from transform_to_clean import transform_and_load_clean

def run_pipeline(days):
    print("ETL boshlandi...")
    extract_cbu_data(days_back=days)
    transform_and_load_clean()
    print("ETL muvaffaqiyatli yakunlandi.")

if __name__ == "__main__":
    
    run_pipeline(0)
    