import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("clinical_data.csv")

# Clean columns
df['patient_id'] = df['patient_id'].astype(str).str.strip()
df['age_at_Imaging (years)'] = pd.to_numeric(df['age_at_Imaging (years)'], errors='coerce')

# Drop missing ages
df = df.dropna(subset=['age_at_Imaging (years)'])

# Get minimum age per patient
df_min = df.groupby('patient_id')['age_at_Imaging (years)'].min()

# Plot histogram
plt.figure()
plt.hist(df_min, bins=range(0, 101, 10))  # 10-year bins

plt.xlabel("Age (years)")
plt.ylabel("Count")
plt.title("Age Distribution")

plt.grid(axis='y')

# Save image
plt.savefig("age_hist.png")

plt.show()