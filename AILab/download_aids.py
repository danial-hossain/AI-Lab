import pandas as pd
import urllib.request
import ssl

# Disable SSL certificate verification
ssl._create_default_https_context = ssl._create_unverified_context

# UCI dataset URL
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00540/AIDS_Classification.csv"

# Download dataset
data = pd.read_csv(url)

# Save as CSV
data.to_csv("aids_dataset.csv", index=False)

print("Dataset saved successfully!")
print("Dataset shape:", data.shape)
print(data.head())