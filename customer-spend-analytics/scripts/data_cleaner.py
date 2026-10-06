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

    df.columns=df.columns.str.strip()


    df['Income'] = (
        df['Income']
        .str.replace('$', '', regex=False)
        .str.replace(',', '', regex=False)
        .str.strip()
        .replace('', pd.NA)
        .astype(float)
    )

   
    

    df = df.dropna(subset='Income').copy()

    df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%m/%d/%y')

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


    df['Country'] = df['Country'].map(country_code_mapping)

  
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

    df['Total_Spend'] = (
        df['MntWines'] + df['MntFruits'] + df['MntMeatProducts']
        + df['MntFishProducts'] + df['MntSweetProducts'] + df['MntGoldProds']
    )

    current_year = datetime.now().year

    df['Age_Group'] = [
        'Senior' if (current_year - year) > 50 else 'Adult'
        for year in df['Year_Birth']
    ]
    return df
