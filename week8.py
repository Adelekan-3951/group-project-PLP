# Let's create a complete solution for the assignment using the Iris dataset from sklearn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Save to CSV (simulating loading from a file)
df.to_csv("/mnt/data/iris_dataset.csv", index=False)

# Load CSV using pandas (with try/except for error handling)
try:
    data = pd.read_csv("/mnt/data/iris_dataset.csv")
    print("Dataset loaded successfully.\n")
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
except Exception as e:
    print(f"An error occurred: {e}")

# Display first few rows
print("First 5 rows of the dataset:")
display(data.head())

# Explore structure and check for missing values
print("\nDataset Info:")
data_info = data.info()

print("\nMissing values in each column:")
missing_values = data.isnull().sum()

# Basic statistics
print("\nBasic Statistics:")
describe_stats = data.describe()

# Group by species and calculate mean of features
print("\nMean values per species:")
species_group_mean = data.groupby('species').mean()

# Visualizations
plt.figure(figsize=(16, 12))

# Line plot - using average petal length over samples
plt.subplot(2, 2, 1)
plt.plot(data['petal length (cm)'], label='Petal Length')
plt.title("Line Chart of Petal Length")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")
plt.legend()

# Bar chart - average sepal length per species
plt.subplot(2, 2, 2)
sns.barplot(x='species', y='sepal length (cm)', data=data)
plt.title("Bar Chart: Avg Sepal Length per Species")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")

# Histogram - distribution of sepal width
plt.subplot(2, 2, 3)
plt.hist(data['sepal width (cm)'], bins=15, color='orange')
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")

# Scatter plot - sepal length vs petal length
plt.subplot(2, 2, 4)
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=data)
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")

plt.tight_layout()
plt.show()

# Return insights and summaries
(data_info, missing_values, describe_stats, species_group_mean)