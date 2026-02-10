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


cursor = conn.cursor()   

cursor.execute("""
    SELECT 
        age_group,
        AVG(social_media_hours)
    FROM internet_usage
    GROUP BY age_group
""")
results1=cursor.fetchall()
print("Avergae daily usage hours by age:", results1)
#This query finds the average daily sceen time of 
cursor.execute("""
   SELECT 
    age_group,
    AVG(total_screen_time)
FROM internet_usage
GROUP BY age_group;
SORT BY ASC
""")
results_2 = cursor.fetchall()
print("Average screentime for ech age group:", results_2)


conn.close()

