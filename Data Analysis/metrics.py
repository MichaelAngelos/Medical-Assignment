import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("clinical_data.csv")

# Clean
df['patient_id'] = df['patient_id'].astype(str).str.strip()

# Count visits per patient
visits = df['patient_id'].value_counts()

print("Total Patients:", len(visits))

print("Total Visits:", len(df['patient_id']))