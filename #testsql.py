#testsql
import pandas as pd
import os
import kagglehub

path = kagglehub.dataset_download(
    "jayjoshi37/daily-internet-usage-statistics-by-age-group"
)

csv_file = os.path.join(path, "daily_internet_usage_by_age_group.csv")

df = pd.read_csv(csv_file)

print(df.head())
print(df.columns)

import sqlite3

conn = sqlite3.connect("internet_usage.db")
df.to_sql("internet_usage", conn, if_exists="replace", index=False)
import sqlite3

conn = sqlite3.connect("internet_usage.db")
cursor = conn.cursor()

# Query 1: Average age by internet type
cursor.execute("""
    SELECT internet_type, AVG(age) AS avg_age
    FROM internet_usage
    GROUP BY internet_type
""")
results1 = cursor.fetchall()
print("Average age by internet type:", results1)

# Query 2: Average total screen time by age group
cursor.execute("""
    SELECT age_group, AVG(total_screen_time) AS avg_screen_time
    FROM internet_usage
    GROUP BY age_group
""")
results2 = cursor.fetchall()
print("Average screen time by age group:", results2)

conn.close()
