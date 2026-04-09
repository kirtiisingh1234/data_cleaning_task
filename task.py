import numpy as np
import pandas as pd
df=pd.read_csv("netflix_titles.csv")
print(df.head())
# checking missing values
print(df.isnull().sum())
#filling director column value

df['director'] = df['director'].fillna("Unknown")
df['cast'] = df['cast'].fillna("Not Available")
df['country'] = df['country'].fillna("Unknown")
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['date_added'] = df['date_added'].fillna(method='ffill')

df['duration_num'] = df['duration'].str.extract(r'(\d+)')
df['duration_type'] = df['duration'].str.extract(r'([A-Za-z]+)')

df['duration_num'] = df['duration_num'].fillna(0).astype(int)
df['duration_type'] = df['duration_type'].fillna("Unknown")
df['rating'] = df['rating'].fillna(df['rating'].mode()[0])
print(df.isnull().sum())
#removing duplicate
df = df.drop_duplicates()
#date format
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
print(df["date_added"])

#rename column header
df.columns = df.columns.str.lower().str.replace(" ", "_")
print(df.head())

df.to_csv("cleaned_netflix.csv", index=False)

print("Data Cleaning Done")





