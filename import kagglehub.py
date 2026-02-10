import kagglehub
import os

path = kagglehub.dataset_download(
    "jayjoshi37/daily-internet-usage-statistics-by-age-group"
)

print("Dataset path:", path)
print("Files in directory:")
for f in os.listdir(path):
    print(f)
