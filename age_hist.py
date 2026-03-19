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
import numpy as np
import matplotlib.pyplot as plt

bins = np.arange(0, 101, 10)

# Histogram data
counts, edges = np.histogram(df_min, bins=bins)

plt.figure()

# Draw bars
plt.bar(edges[:-1], counts,
        width=np.diff(edges),
        align='edge',
        edgecolor='black')

# Create range labels
labels = [f"{int(edges[i])}-{int(edges[i+1]-1)}" for i in range(len(edges)-1)]

# Set ticks at bin centers
centers = edges[:-1] + np.diff(edges)/2
plt.xticks(centers, labels, rotation=45)

plt.xlabel("Age range")
plt.ylabel("Count")
plt.title("Age Distribution")

plt.grid(axis='y')

plt.tight_layout()
plt.savefig("age_hist.png")
plt.show()