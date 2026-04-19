import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("random_walk.csv")
df["distance"] = np.sqrt(df["x"]**2 + df["y"]**2)
print(df["distance"].max())
print(df["distance"].mean())
# print(df.head())

filtered = df[df["distance"]>df["distance"].mean()]
print(filtered.head())
filtered.to_json("filtered.json", orient="records", indent = 2)