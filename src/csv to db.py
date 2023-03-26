import pandas as pd
from sqlalchemy import create_engine
from models import db, Store, BusinessHours, StoreStatus
from app import app

# Read data from CSV files
store_df = pd.read_csv('stores.csv')
business_hours_df = pd.read_csv('business_hours.csv')
store_status_df = pd.read_csv('store_status.csv')

# Connect to SQLite database
engine = create_engine('sqlite:///database.db')
with app.app_context():
    db.create_all()

# Insert data into SQLite database
store_df.to_sql('store', con=engine, if_exists='append', index=False)
business_hours_df.to_sql('business_hours', con=engine, if_exists='append', index=False)
store_status_df.to_sql('store_status', con=engine, if_exists='append', index=False)
