# Customer Segmentation Using Clustering

## 📌 Project Overview
Customer segmentation is a key marketing strategy that helps businesses understand their customers better. This project leverages **K-Means Clustering** to categorize customers based on their purchasing behavior, enabling companies to optimize marketing efforts, enhance customer engagement, and improve resource allocation.

## 📂 Dataset Information
- **Dataset Name:** `customer_data.csv`
- **Columns:**
  - `Customer ID` - Unique identifier for each customer
  - `Age` - Age of the customer
  - `Annual Income` - Customer's annual income (in dollars or any currency)
  - `Spending Score` - A metric assigned based on spending behavior

## 🔹 Project Workflow

### 1️⃣ Data Loading & Exploration
- Loaded the dataset using **Pandas**.
- Examined data structure, checked for **missing values, duplicates, data types**, and reviewed summary statistics.

### 2️⃣ Data Preprocessing
- Removed **duplicate records** to ensure clean data.
- Standardized numerical features using **StandardScaler** to maintain uniform scale and improve clustering performance.

### 3️⃣ Clustering Analysis
- **Determined the optimal number of clusters**:
  - Used the **Elbow Method** to identify the ideal `k` by analyzing the Within-Cluster Sum of Squares (WCSS).
  - Evaluated cluster quality using the **Silhouette Score**.
- **Applied K-Means Clustering**:
  - Trained the model using the optimal number of clusters.
  - Assigned cluster labels to customers for further analysis.

### 4️⃣ Data Visualization & Interpretation
- **Elbow Method Plot** to visualize the optimal number of clusters.
- **2D Scatter Plot** using **Principal Component Analysis (PCA)** to illustrate customer segments.
- **Cluster Representations** with distinct colors to aid in interpretation.

## 📊 Results & Business Insights
- Successfully segmented customers into meaningful groups based on purchasing behavior.
- Identified **high-value customers** for potential loyalty programs.
- Recommended **targeted marketing strategies** based on age and income groups.
- Provided data-driven insights for **customer engagement and sales growth**.

## 📁 Project Deliverables
- **Clustered Dataset:** Updated dataset with a `Cluster` column, saved as `updated_customer_data.csv`.
- **Visualizations:**
  - Elbow Method Plot
  - 2D Scatter Plot of clusters using PCA
- **Actionable Insights:** Business recommendations based on customer segmentation.

## 🛠 Technologies & Tools Used
- **Programming Language:** Python 🐍
- **Libraries:**
  - **Data Handling:** Pandas, NumPy
  - **Visualization:** Matplotlib, Seaborn
  - **Machine Learning:** Scikit-Learn (K-Means Clustering, PCA, StandardScaler)

## 📌 Conclusion
Customer segmentation plays a vital role in business strategy. This project effectively groups customers based on spending behavior, enabling businesses to tailor marketing campaigns and enhance customer relationships. The use of **K-Means Clustering and PCA** provides valuable insights for data-driven decision-making. 🚀

## 🔗 Connect with Me
[LinkedIn Profile](https://www.linkedin.com/in/s-berlin-samvel-pandian007)

---
**Author:** Berlin Samvel Pandian S

#DataScience #MachineLearning #KMeans #CustomerSegmentation #Python #DataAnalysis
