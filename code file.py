import wrds
import pandas as pd
username = "linngyao"
db = wrds.Connection(wrds_username="linngyao")
query = """
SELECT gvkey, conm, fic, sic, naics
FROM comp.company
WHERE fic IS NOT NULL
LIMIT 1000
"""
df = db.raw_sql(query)

print("===== First 5 rows =====")
print(df.head())

print("\n===== Data Shape =====")
print(df.shape)
df = df.drop_duplicates()
df = df.dropna(subset=["fic"])

print("\n===== Shape After Cleaning =====")
print(df.shape)
country_counts = df["fic"].value_counts().head(10)

print("\n===== Top 10 Countries =====")
print(country_counts)

import matplotlib.pyplot as plta
plt.figure(figsize=(10, 6))
country_counts.sort_values().plot(kind="barh")
plt.title("Top 10 Countries by Number of Firms (Compustat)")
plt.xlabel("Number of Firms")
plt.ylabel("Country Code")
plt.tight_layout()
plt.show()

if "sic" in df.columns:
    df = df[df["sic"].notna()].copy()
    df["sic"] = df["sic"].astype(str)
    df["sic2"] = df["sic"].str[:2]

    sic_counts = df["sic2"].value_counts().head(10)

    print("\n===== Top 10 SIC 2-digit Groups =====")
    print(sic_counts)

    plt.figure(figsize=(10, 6))
    sic_counts.sort_values().plot(kind="barh")
    plt.title("Top 10 Industry Groups by SIC 2-digit Code")
    plt.xlabel("Number of Firms")
    plt.ylabel("SIC 2-digit Code")
    plt.tight_layout()
    plt.show()
top_country = country_counts.index[0]
top_country_num = country_counts.iloc[0]

print("\n===== Business Insights =====")
print(f"1. {top_country} has the largest number of firms in this WRDS sample ({top_country_num}).")
print("2. The cross-country distribution suggests that listed firms are concentrated in a small number of major markets.")
print("3. Industry clustering can be observed through SIC group counts, which helps explain the economic structure of the sample.")
print("4. This project shows how WRDS and Python can transform raw firm data into business insights.")
print("\n===== Short English Summary for Video =====")
print("This project uses WRDS and Python to analyze the distribution of firms across countries and industries.")
print(f"The results show that {top_country} has the highest number of firms in the sample.")
print("The analysis also reveals industry concentration through SIC group distribution.")
print("This demonstrates how Python can extract and communicate business insights directly from WRDS data.")

db.close()
