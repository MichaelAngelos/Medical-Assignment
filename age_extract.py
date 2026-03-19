import pandas as pd

# Load data
df = pd.read_csv("clinical_data.csv")

# Clean columns (important)
df['patient_id'] = df['patient_id'].astype(str).str.strip()
df['age_at_Imaging (years)'] = pd.to_numeric(df['age_at_Imaging (years)'], errors='coerce')

# Drop rows with missing age
df = df.dropna(subset=['age_at_Imaging (years)'])

# Get minimum age per patient
df_min = df.groupby('patient_id', as_index=False)['age_at_Imaging (years)'].min()

# Count how many patients per age
age_counts = df_min['age_at_Imaging (years)'].value_counts().sort_index()

# Convert to dataframe
age_counts_df = age_counts.reset_index()
age_counts_df.columns = ['age', 'count']

# Save to CSV (gnuplot-friendly)
age_counts_df.to_csv("age_counts.csv", index=False, header=False)

print("Saved age_counts.csv")