# Airbnb-Market Segments with K-Means Clustering

🧾 Introduction

Airbnb.com, a global company engaged in the short-term rental of accommodations, that connects property owners (hosts) with guests looking for accommodation.
With increasing competition and the need for personalized service,  it is important to understand the types or segments of listings available on their platform. 

📌 Project Overview
This project aims to segment Airbnb listings in New York City using unsupervised machine learning techniques (mainly K-Means Clustering) based on key listing features such as price, availability, and review metrics.

✅ Objectives

🔍 Understand listing patterns and segment them into distinct clusters

🧠 Provide business insights for Airbnb stakeholders (pricing, engagement)

🛠️ Build an end-to-end clustering pipeline including preprocessing, modeling,
    visualization and building an interactive dashboard for data exploration and segmentation using Streamlit.

✅ Goals
- Perform EDA (Exploratory Data Analysis)
- Clean and preprocess the dataset
- Handle missing values and outliers
- Implement K-Means clustering and evaluate with silhouette score
- Apply scaling and dimensionality reduction
- Interpret and visualize each cluster
- Build an interactive dashboard with Streamlit
  
Result : 

CLuster 0 🔴 = Populer
This Cluster represents properties with affordable prices but high occupancy rates. Listings in this cluster perform very well in terms of number of reviews and rental frequency, indicating high appeal among budget travelers.

CLuster 1 🟡 = Dormant 
This cluster reflects listings with low rental activity. This is likely due to lack of visibility, less competitive pricing, or less strategic location.

Cluster 2 🔵 = Premium 
This Cluster consists of exclusive property listings with higher rental rates and high availability. Targeting the upper-end market segment with a preference for comfort and quality of service.

Model deployment with Streamlit link: https://airbnb-market-segments-with-k-means-clustering.streamlit.app/
