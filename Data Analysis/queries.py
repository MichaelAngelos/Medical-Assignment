import pandas as pd

# Load CSV
df = pd.read_csv("clinical_data.csv")

# Clean up (important if messy CSV)
df['sex'] = df['sex'].str.strip()

# Count
counts = df['sex'].value_counts()

# Convert to percentage
percentages = counts / counts.sum() * 100

print(percentages)