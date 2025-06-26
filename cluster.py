import requests
import joblib 
import os
import streamlit as st
import pandas as pd
import pickle
import warnings
from sklearn.preprocessing import PolynomialFeatures
from numerize import numerize


def predict():
    model = joblib.load('kmeans_airbnb.joblib')
        
    st.markdown("""
        <h1 style="color:Grey; text-align:left;">🧠 Airbnb Market Cluster</h1>
        <p style="text-align:justify;">
        Gunakan form di bawah untuk mengelompokkan listing ke dalam <b>klaster market Airbnb</b> berdasarkan karakteristik utama properti. """, unsafe_allow_html=True)
    
    # Form input fitur 
    with st.form('Prediction Form'):
        st.markdown("#### 📋 Input informasi Properti")
        col1, col2 = st.columns(2)
        with col1:
            price = st.number_input("💰 Harga per malam", min_value=10, max_value=10000, value=150)
            reviews_per_month = st.number_input("📅 Review per bulan", min_value=0, max_value=30, value=1)
            listings = st.number_input("🏠 Jumlah listing host", min_value=1, max_value=100, value=2)
        with col2:
            min_nights = st.slider("🌙 Minimum Nights", 1, 60, 3)
            availability = st.slider("📆 Ketersediaan per tahun", 0, 365, 180)
            reviews = st.slider("📝 Jumlah review", 0, 500, 50)
        submitted = st.form_submit_button("🎯 Prediksi Klaster")

     # Mapping deskripsi klaster
    cluster_info = {
        0: {
            "label": " Klaster 0 ⭐**Populer**",
            "desc": """Klaster ini merepresentasikan properti dengan harga terjangkau namun memiliki tingkat okupansi tinggi. 
             Listing pada klaster ini menunjukkan performa sangat baik dari sisi jumlah ulasan dan frekuensi penyewaan, 
             mengindikasikan daya tarik kuat di kalangan wisatawan dengan anggaran terbatas."""},
        1: {
            "label": "Klaster 1 💤**Dormant**",
            "desc": """Klaster ini mencerminkan listing dengan aktivitas penyewaan yang rendah. 
             Kemungkinan disebabkan oleh kurangnya visibilitas, harga yang kurang kompetitif, atau lokasi yang kurang strategis."""},
        2: {
            "label": "Klaster 2  🏙️**Premium**",
            "desc": """Klaster ini terdiri dari properti eksklusif dengan tarif sewa lebih tinggi dan tingkat ketersediaan yang luas. 
             Menargetkan segmen pasar kelas atas dengan preferensi kenyamanan, privasi dan kualitas layanan yang unggul."""}}

    # Prediksi
    if submitted:
        input_df = pd.DataFrame([[
            price,
            min_nights,
            reviews,
            reviews_per_month,
            listings,
            availability]], 
            columns=[
            'price',
            'minimum_nights',
            'number_of_reviews',
            'reviews_per_month',
            'calculated_host_listings_count',
            'availability_365'])

        cluster_pred = model.predict(input_df)[0]
        info = cluster_info.get(cluster_pred)

        st.success(f"🏷️ Listing ini termasuk dalam {info['label']}")
        st.markdown(f"**Deskripsi Klaster:**\n\n{info['desc']}")


