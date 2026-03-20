import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("clinical_data.csv")

# Clean
df['patient_id'] = df['patient_id'].astype(str).str.strip()

# Count visits per patient
visits = df['patient_id'].value_counts()

# Plot histogram
plt.figure()
plt.hist(visits, bins=range(1, visits.max()+2))

plt.xlabel("Number of visits per patient")
plt.ylabel("Number of patients")
plt.title("Visits per Patient Distribution")

plt.grid(axis='y')

plt.savefig("visits_hist.png")
plt.show()