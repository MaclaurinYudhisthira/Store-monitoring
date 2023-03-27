import pandas as pd
from sqlalchemy import create_engine
from models import db, Timezone, BusinessHours, Store_status
from app import app

# Read data from CSV files
timezone_df = pd.read_csv('E:\\Kishan Dasondhi\\Work\\Store-monitoring\\CSV files\\time zones.csv')
business_hours_df = pd.read_csv('E:\\Kishan Dasondhi\\Work\\Store-monitoring\\CSV files\\Menu hours.csv')
store_status_df = pd.read_csv('E:\\Kishan Dasondhi\\Work\\Store-monitoring\\CSV files\\store status.csv')

# Connect to SQLite database
engine = create_engine('sqlite:///E:\Kishan Dasondhi\Work\Store-monitoring\src\instance\database.db')
with app.app_context():
    db.create_all()

# Insert data into SQLite database
store_status_df.to_sql('store_status', con=engine, if_exists='append', index=False)
timezone_df.to_sql('timezone', con=engine, if_exists='append', index=False)
business_hours_df.to_sql('businesshours', con=engine, if_exists='append', index=False)

