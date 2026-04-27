import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("clinical_data.csv")

# Clean
df['patient_id'] = df['patient_id'].astype(str).str.strip()

# Convert datetime
df['study_datetime'] = pd.to_datetime(
    df['study_datetime'],
    format="%Y-%m-%d_%H-%M-%S",
    errors='coerce'
)

# Drop invalid dates
df = df.dropna(subset=['study_datetime'])

# Compute time span per patient
time_span = df.groupby('patient_id')['study_datetime'].agg(['min', 'max'])

# Calculate difference (in days)
time_span['days'] = (time_span['max'] - time_span['min']).dt.days

# Remove patients with only one visit (0 days)
time_span = time_span[time_span['days'] > 0]

# Histogram
plt.figure()
plt.hist(time_span['days'], bins=20)

plt.xlabel("Time between first and last visit (days)")
plt.ylabel("Number of patients")
plt.title("Follow-up Duration per Patient")

plt.grid(axis='y')

plt.savefig("time_between_visits.png")
plt.show()