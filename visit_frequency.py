import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("clinical_data.csv")

# Clean
df['patient_id'] = df['patient_id'].astype(str).str.strip()
df['study_datetime'] = pd.to_datetime(
    df['study_datetime'],
    format="%Y-%m-%d_%H-%M-%S",
    errors='coerce'
)

df = df.dropna(subset=['study_datetime'])

# Visits per patient
visits = df['patient_id'].value_counts()

# Time span per patient
time_span = df.groupby('patient_id')['study_datetime'].agg(['min', 'max'])
time_span['days'] = (time_span['max'] - time_span['min']).dt.days

# Merge visits
time_span['visits'] = visits

# Compute frequency (visits per month)
time_span['frequency'] = 0.0  # initialize

mask = time_span['days'] > 0
time_span.loc[mask, 'frequency'] = (
    time_span.loc[mask, 'visits'] / (time_span.loc[mask, 'days'] / 30)
)

# Histogram
plt.figure()
plt.hist(time_span['frequency'], bins=20)

plt.xlabel("Visit frequency (visits per month)")
plt.ylabel("Number of patients")
plt.title("Visit Frequency Distribution")

plt.grid(axis='y')

plt.savefig("visit_frequency.png")
plt.show()

# Optional: print summary
print(time_span['frequency'].describe())