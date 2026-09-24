# Customer Spend by Market and Profile

A Python pipeline and Power BI dashboard analysing 2,216 customers across 8 markets to show who spends the most, where they are, and how they respond to campaigns.



## Business context and objective

A retailer wants to know which customers and markets create the most value so it can aim its marketing budget better. This project cleans the customer data, enriches it with country information from an API, and turns it into a one-page dashboard that supports targeting and campaign decisions.

## Key questions

1. How much do customers spend overall, and how many respond to campaigns?
2. Which markets and regions drive the most spend?
3. How does income affect spend?
4. How does household size affect spend?
5. Which products make up most of the spend?

## Insights

1. **Overall performance:** A total of 2,216 customers spent 1,345,279, which averages to 607 per customer. 15% Of the audience accepted the latest campaign. This shows that most customers are not responding to the campaign.

2. **Markets:** Europe makes up 54% of the spend. Spain alone accounts for half of the total spending. South Africa contributes around 0.21 million. Canada around 0.17 million. Mexico has a low contribution. Its results are not meaningful. Should not be overinterpreted.

3. **Income:** The average spend varies greatly by income. Customers earning under 30k spend 72 on average. Those earning above 90k spend 1,575, which's about 22 times more. Income is clearly the indicator of customer value in this data.

4. **Household size:** Customers with no children spend 1,105 on average. This is 4.5 times higher than customers with two children, who spend 247. Households with children spend less regardless of income level.

5. **Products:** Wine accounts for about half of all spending and meat makes up about 28%. These two product categories together carry most of the revenue.

## Recommendations

- Focus on high-income households that do not have children when planning campaigns. These customers show the spending levels.

- Look into why 15% of customers responded. Test offers for each customer segment before increasing the campaign budget.

- When considering shifting budget between markets compare spend per customer instead of just total spend. Spain’s lead may come from having customers rather than higher spending, per customer.

## Data

- **Source:** Kaggle marketing dataset with a `Country` column (`marketing_data.csv`).

- **Files produced:** `cleaned_marketing_data.csv` (customers) and `country_reference.csv` (region, currency and population per country).

- **Cleaning:** removes missing income values converts dates, drops birth years groups junk marital-status values as "Unknown" and maps the datasets country codes, to ISO codes.

## Pipeline

Load the CSV clean it engineer features (`Total_Spend` `Age_Group`) enrich each country through the REST Countries API save both outputs then load them into Power BI.

## Data model

`Dim_Country` (one) to `Fact_Customers` (many) on country code, single-direction filter.


## Tech stack

Python (pandas, requests, python-dotenv), REST Countries API, DAX, Power BI.
