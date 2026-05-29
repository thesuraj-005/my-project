import pandas as pd
import numpy as np
import re


print("1) REGEX PATTERNS")

email = "test@gmail.com"
mobile = "9876543210"
name = "Suraj"

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
mobile_pattern = r'^[6-9]\d{9}$'
name_pattern = r'^[A-Za-z]+$'

print("Email Valid:", bool(re.match(email_pattern, email)))
print("Mobile Valid:", bool(re.match(mobile_pattern, mobile)))
print("Name Valid:", bool(re.match(name_pattern, name)))


print("\n2) DATETIME FUNCTIONS IN PANDAS")

dates = pd.Series(['2026-05-29', '2026-06-15', '2026-07-20'])

dates = pd.to_datetime(dates)

print(dates)

print("\nYear:")
print(dates.dt.year)

print("\nMonth:")
print(dates.dt.month)

print("\nDay:")
print(dates.dt.day)

print("\nDay Name:")
print(dates.dt.day_name())

print("\nMonth Name:")
print(dates.dt.month_name())


print("\n3) CSV FILE DATA CLEANING AND ANALYSIS")

df = pd.read_csv("tips.csv")

print("\nOriginal Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

df = df.drop_duplicates()

numeric_cols = df.select_dtypes(include=np.number).columns

for col in numeric_cols:
    df[col].fillna(df[col].mean(), inplace=True)

print("\nCleaned Data:")
print(df)

print("\nBasic Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nAverage Total Bill:")
print(df['total_bill'].mean())

print("\nHighest Tip:")
print(df['tip'].max())

print("\nRows where Tip is greater than 5:")
print(df[df['tip'] > 5])

print("\nGroup By Gender Average Tip:")
print(df.groupby('sex')['tip'].mean())