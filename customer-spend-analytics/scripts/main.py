import pandas as pd
from datetime import datetime
import requests 
import os
from dotenv import load_dotenv


from data_loader import load_files
from data_cleaner import clean_data, add_features
from api_client import get_country_info
from file_saver import save_data, save_country_data

# Load API key from .env — never hardcoded, never committed to Git
load_dotenv()
API_KEY = os.getenv('RESTCOUNTRIES_API_KEY')

# --- Load and process the customer dataset ---
data = load_files(r'C:\Users\ayari\Downloads\python projects\customer-spend-analytics\data\marketing_data.csv')
data=clean_data(data)
data=add_features(data)

# --- Enrich a small set of countries via the REST Countries API ---
cache = {}
country_codes = ['ES', 'CA', 'US', 'AU', 'DE', 'IN', 'ZA','MX']
for country_code in country_codes : 
    get_country_info(country_code,cache,API_KEY) 

# --- Save both outputs, ready for Power BI ---
save_country_data(cache,r'C:\Users\ayari\Downloads\python projects\customer-spend-analytics\output\country_reference.csv') 
save_data(data,r'C:\Users\ayari\Downloads\python projects\customer-spend-analytics\output\cleaned_marketing_data.csv')
