# Customer Segmentation using Clustering

## 📌 Project Overview
This project focuses on **customer segmentation** using **K-Means Clustering** to group customers based on their purchasing behavior. By identifying meaningful customer clusters, businesses can **enhance marketing strategies, optimize resource allocation, and improve customer engagement**.

## 📂 Dataset Information
- **Dataset Name:** `customer_data.csv`
- **Columns:**
  - `Customer ID` - Unique identifier for each customer
  - `Age` - Age of the customer
  - `Annual Income` - Customer's income in $ (or any currency)
  - `Spending Score` - A score assigned based on spending behavior

## 🔹 Project Steps

### 1️⃣ Load the Dataset
- Used **Pandas** to load and inspect the dataset.
- Checked for **missing values, duplicates, data types, and summary statistics**.

### 2️⃣ Data Preprocessing
- Standardized the data using **StandardScaler** from `sklearn` to normalize features.
- Ensured all features are on the same scale for better clustering performance.

### 3️⃣ Clustering Analysis
- **Determined the optimal number of clusters**:
  - Used the **Elbow Method** (WCSS vs. number of clusters).
  - Used **Silhouette Score** for further validation.
- **Applied K-Means Clustering**:
  - Trained the model with the optimal number of clusters.
  - Assigned cluster labels to each customer.

### 4️⃣ Data Visualization
- **Elbow Method Plot** to identify the optimal cluster count.
- **2D Scatter Plot** of clusters using **PCA (Principal Component Analysis)**.
- **Pair Plots** to visualize feature relationships within clusters.
- **Centroid Visualization** to interpret cluster centers.

## 📊 Results & Insights
- Successfully segmented customers into distinct groups based on purchasing patterns.
- Identified **high-spending customers** who could be targeted for loyalty programs.
- Suggested tailored marketing strategies for different age and income groups.

## 📁 Deliverables
- **Clustered Dataset**: Added a new column with assigned cluster labels.
- **Visualizations**: Elbow method plot, 2D scatter plot, and pair plots.
- **Actionable Insights** for businesses to optimize marketing and sales strategies.

## 🛠 Technologies Used
- **Python** 🐍
- **Pandas, NumPy** (Data Handling)
- **Matplotlib, Seaborn** (Data Visualization)
- **Scikit-Learn** (Machine Learning & Clustering)

## 📌 Conclusion
This project demonstrates how clustering techniques can help businesses **understand customer behavior and improve decision-making**. By segmenting customers effectively, companies can create **personalized marketing campaigns** and increase customer engagement. 🚀

## 🔗 Connect with Me
[LinkedIn Profile](https://www.linkedin.com/in/s-berlin-samvel-pandian007)  

---
**Author:** Berlin Samvel Pandian S

#DataScience #MachineLearning #KMeans #CustomerSegmentation #Python #DataAnalysis
