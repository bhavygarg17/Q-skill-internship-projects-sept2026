import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Display dataset
print("===== DATA ANALYSIS PROJECT =====")
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# Average measurements by flower species
print("\nAverage Values by Species:")
print(df.groupby("species").mean(numeric_only=True))

# Bar Chart
df.groupby("species")["sepal_length"].mean().plot(
    kind="bar", title="Average Sepal Length by Species"
)
plt.ylabel("Sepal Length")
plt.tight_layout()
plt.show()

# Scatter Plot
for species, group in df.groupby("species"):
    plt.scatter(
        group["sepal_length"],
        group["petal_length"],
        label=species
    )

plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.legend()
plt.tight_layout()
plt.show()

# Correlation Heatmap using Matplotlib
correlation = df.select_dtypes(include="number").corr()

plt.imshow(correlation, cmap="coolwarm", vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlation.columns)), correlation.columns,
           rotation=45, ha="right")
plt.yticks(range(len(correlation.columns)), correlation.columns)
plt.title("Feature Correlation Heatmap")

for i in range(len(correlation.columns)):
    for j in range(len(correlation.columns)):
        plt.text(j, i, f"{correlation.iloc[i, j]:.2f}",
                 ha="center", va="center", fontsize=8)

plt.tight_layout()
plt.show()

print("\nData analysis completed successfully!")
  
