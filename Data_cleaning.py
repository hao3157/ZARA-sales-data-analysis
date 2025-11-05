import pandas as pd
# Read file
df = pd.read_csv("Zara_sales_EDA.csv", sep=";")
print(df.info()
df.to_csv('ZARA_sales_dataset.csv', index=False)
