import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

# Step 1: Load the Dataset
df = pd.read_csv("customer_data.csv")
print("Initial Data:")
print(df.head())

print("\nData Types:\n", df.dtypes)

print(" The shape of the dataset is ", df.shape)

print(" The summary statistics of the dataset is \n", df.describe())

# Step 2: Data Preprocessing
print("\nChecking for missing values:")
print(df.isnull().sum())

df.drop_duplicates(inplace=True)  # Remove duplicates

# Selecting numerical features for clustering
features = ['Age', 'Annual Income', 'Spending Score']
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df[features])

# Step 3: Determine Optimal Clusters
wcss = []
k_values = range(1, 11)
for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(df_scaled)
    wcss.append(kmeans.inertia_)

# Elbow Method Plot
plt.figure(figsize=(8,5))
plt.subplot(2,2,1)
plt.plot(k_values, wcss, marker='o', linestyle='--')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.title('Elbow Method for Optimal k')

# Choosing optimal k based on elbow point (let's assume k=4 after analyzing the plot)
k_optimal = 4
kmeans = KMeans(n_clusters=k_optimal, random_state=42, n_init=10)
df['Cluster'] = kmeans.fit_predict(df_scaled)

# Silhouette Score
total_score = silhouette_score(df_scaled, df['Cluster'])
print(f"Silhouette Score for k={k_optimal}: {total_score:.4f}")

# Step 4: Visualization
pca = PCA(n_components=2)
df_pca = pca.fit_transform(df_scaled)
df['PCA1'], df['PCA2'] = df_pca[:, 0], df_pca[:, 1]

plt.subplot(2,2,2)
sns.scatterplot(x='PCA1', y='PCA2', hue=df['Cluster'], palette='viridis', data=df, s=100)
plt.title('Customer Segmentation using K-Means')
plt.tight_layout()
plt.show()

# Save the clustered dataset
df.to_csv("updated_customer_data.csv", index=False)
print("Clustered dataset saved as customer_data_clustered.csv")
