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

plt.figure(figsize=(9, 7))
plt.plot(df["x"], df["y"], color = "pink", linewidth = 2,
         linestyle = "-", alpha = 0.67, label = "траєкторія")
plt.scatter(df["x"][:1], df["y"][:1], color = "deeppink", s = 100, label = "початок")
plt.scatter(df["x"][-1:], df["y"][-1:], color = "deeppink", s = 100, marker = "x", label = "кінець")
plt.title("Траєкторія випадкового блукання")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
