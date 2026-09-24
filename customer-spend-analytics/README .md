# Customer Spend by Market and Profile

A Python pipeline and Power BI dashboard analysing 2,216 customers across 8 markets to show who spends the most, where they are, and how they respond to campaigns.

![Dashboard](images/dashboard.png)

## Business context and objective

A retailer wants to know which customers and markets create the most value so it can aim its marketing budget better. This project cleans the customer data, enriches it with country information from an API, and turns it into a one-page dashboard that supports targeting and campaign decisions.

## Key questions

1. How much do customers spend overall, and how many respond to campaigns?
2. Which markets and regions drive the most spend?
3. How does income affect spend?
4. How does household size affect spend?
5. Which products make up most of the spend?

## Insights

1. **Overall performance:** 2,216 customers spent 1,345,279 in total, or 607 per customer on average. Only 15% accepted the latest campaign, so most of the audience is not responding.
2. **Markets:** Europe accounts for 54% of spend, and Spain alone is roughly half of the total. South Africa (about 0.21M) and Canada (about 0.17M) follow. Mexico is negligible, so its results should not be over-read.
3. **Income:** average spend climbs from 72 for customers under 30k to 1,575 for customers above 90k, about 22x higher. Income is the strongest signal of customer value in this data.
4. **Household size:** customers with no children spend 1,105 on average, about 4.5x more than customers with two children (247). Households with children spend far less at every level.
5. **Products:** wine makes up about half of all spend and meat about 28%, so two categories carry most of the revenue.

## Recommendations

- Prioritise high-income households without children when targeting campaigns.
- Investigate the low 15% response rate by testing different offers per segment before increasing campaign spend.
- Before shifting budget between markets, compare average spend per customer, not only total spend, because Spain's lead may reflect the number of customers as much as their value.

## Data

- **Source:** Kaggle marketing dataset with a `Country` column (`marketing_data.csv`).
- **Files produced:** `cleaned_marketing_data.csv` (customers) and `country_reference.csv` (region, currency and population per country).
- **Cleaning:** removes missing income values, converts dates, drops implausible birth years, groups junk marital-status values as "Unknown", and maps the dataset's country codes to ISO codes.

## Pipeline

Load the CSV, clean it, engineer features (`Total_Spend`, `Age_Group`), enrich each country through the REST Countries API, save both outputs, then load them into Power BI.

## Data model

`Dim_Country` (one) to `Fact_Customers` (many) on country code, single-direction filter.

## How to run

1. Clone the repository and create a virtual environment.
2. Install the dependencies with `pip install -r requirements.txt`.
3. Download the dataset from Kaggle into `data/raw/`.
4. Copy `.env.example` to `.env` and add your REST Countries API key.
5. Run `python main.py`.
6. Open the Power BI file and refresh the data.

## Limitations

- The data comes from a public Kaggle dataset and the currency of spend is not stated.
- The results show what goes with higher spend, not what causes it.
- Some markets have very few customers, so their averages are unreliable.

## Tech stack

Python (pandas, requests, python-dotenv), REST Countries API, DAX, Power BI.
