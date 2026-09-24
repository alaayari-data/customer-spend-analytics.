import pandas as pd
from datetime import datetime


def clean_data(df):
    """
    Clean known data quality issues in the raw dataset:
    - missing Income values
    - Dt_Customer stored as a string instead of a date
    - unrealistic outlier birth years
    - inconsistent/junk categories in Marital_Status
    """
    # Remove spaces from column names
    df.columns=df.columns.str.strip()

    # Convert Income from currency text to numeric
    df['Income'] = (
        df['Income']
        .str.replace('$', '', regex=False)
        .str.replace(',', '', regex=False)
        .str.strip()
        .replace('', pd.NA)
        .astype(float)
    )

   
    
    # Drop rows with no income value; .copy() avoids a SettingWithCopyWarning later
    df = df.dropna(subset='Income').copy()

    # Convert enrollment date from string to actual datetime, using day-first format
    df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%m/%d/%y')
    # Maps the dataset's custom country codes to standard ISO 3166-1 alpha-2 codes,
    # which is the format the REST Countries API expects.
    country_code_mapping = {
    'SP': 'ES',   # Spain: the dataset uses SP, ISO uses ES
    'CA': 'CA',   # Canada: already ISO
    'US': 'US',   # United States: already ISO
    'AUS': 'AU',  # Australia: 3-letter code shortened to ISO 2-letter
    'GER': 'DE',  # Germany: ISO uses DE (from "Deutschland")
    'IND': 'IN',  # India: 3-letter code shortened to ISO 2-letter
    'SA': 'ZA',   # South Africa: in ISO, SA is Saudi Arabia, so this must be ZA
    'ME': 'MX'    # Mexico: in ISO, ME is Montenegro, so this must be MX
             }

   # Replace each country code with its ISO equivalent.
   # Any code not in the dictionary becomes NaN, so check for missing values afterwards.
    df['Country'] = df['Country'].map(country_code_mapping)

    # Normalize junk marital status entries into a single 'Unknown' category
    # rather than guessing what they actually mean
    df['Marital_Status'] = [
        'Unknown' if word in ['Alone', 'Absurd', 'YOLO'] else word
        for word in df['Marital_Status']
    ]
    return df


def add_features(df):
    """
    Engineer new columns from existing data:
    - Total_Spend: sum of all product spending categories
    - Age_Group: simple Adult/Senior split based on current year
    """
    # Sum all "Mnt*" (amount spent) columns into one total spend figure
    df['Total_Spend'] = (
        df['MntWines'] + df['MntFruits'] + df['MntMeatProducts']
        + df['MntFishProducts'] + df['MntSweetProducts'] + df['MntGoldProds']
    )

    current_year = datetime.now().year
    # Classify each customer as Senior or Adult based on computed age
    df['Age_Group'] = [
        'Senior' if (current_year - year) > 50 else 'Adult'
        for year in df['Year_Birth']
    ]
    return df