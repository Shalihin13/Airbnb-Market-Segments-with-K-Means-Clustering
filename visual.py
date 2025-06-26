import streamlit as st
import pandas as pd
import plotly.express as px

def view_project():
    # Load data
    data = pd.read_csv('AB_NYC_2019.csv')

    # Ambil sampel data untuk tampilan visual 
    data_vis = data.sample(n=1000, random_state=42) if len(data) > 1000 else data

    # Header
    st.markdown("""
        <h1 style='color:Grey;'>🗺️ Airbnb Data Exploration</h1>
    """, unsafe_allow_html=True)
    st.write("Eksplorasi interaktif untuk memahami pola dan karakteristik listing di Airbnb.")

    # Data preview
    with st.expander("📁 Lihat Dataset"):
        st.dataframe(data.sample(200), use_container_width=True)

    # Tabs visualisasi
    tab1, tab2, tab3 = st.tabs(["📊 Visualization", "🌍 Geomap", "⏱️ Last Review"])
    
    # Tab 1: Histogram
    with tab1:
        st.subheader("📊 Distribusi Variabel Numerik")

        # Pilih kolom numerik
        numeric_cols = data_vis.select_dtypes(include='number').columns.tolist()
        col = st.selectbox("🔢 Fitur Numerik", numeric_cols, key="hist")

        # Pilih kolom kategorik opsional
        cat_cols = data_vis.select_dtypes(include='object').nunique()
        # Ambil hanya kategori yang tidak terlalu banyak (maks 20)
        limited_cats = cat_cols[cat_cols <= 20].index.tolist()
        limited_cats.insert(0, "None")
        selected_cat = st.selectbox("🎨 Fitur Kategori (opsional)", limited_cats, key="hist_color")

        # Histogram
        if selected_cat != "None":
            fig = px.histogram(
                data_vis, 
                x=col, 
                color=selected_cat,
                nbins=40,
                color_discrete_sequence=px.colors.qualitative.Set2)
        else:
            fig = px.histogram(
                data_vis,
                x=col,
                nbins=40,
                color_discrete_sequence=["#FF5A5F"])

        fig.update_layout(
            xaxis_title=col,
            yaxis_title='Jumlah',
            bargap=0.1)
        
        st.plotly_chart(fig, use_container_width=True)

    # Tab 2: Geomap
    with tab2:
        st.subheader("📍 Lokasi Listing di Peta")
        fig_map = px.scatter_mapbox(
            data_vis, 
            lat="latitude", 
            lon="longitude",
            hover_name="name",
            hover_data=["neighbourhood_group", "room_type", "price"],
            color="neighbourhood_group",
            zoom=10,
            height=500)
        
        fig_map.update_layout(mapbox_style="carto-positron")
        fig_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig_map, use_container_width=True)

    # Tab 3: Last Review
    with tab3:
        st.subheader("⏱️ Listing dengan Review Terbaru")

        # Pastikan tanggal valid
        data['last_review'] = pd.to_datetime(data['last_review'], errors='coerce')
        latest_data = data.dropna(subset=['last_review'])

        # Filter opsional
        col1, col2 = st.columns(2)
        with col1:
            ng_filter = st.selectbox("🏙️ Neighbourhood Group", ['All'] + sorted(latest_data['neighbourhood_group'].unique()))
        with col2:
            rt_filter = st.selectbox("🛏️ Room Type", ['All'] + sorted(latest_data['room_type'].unique()))

        # Filter data
        filtered = latest_data.copy()
        if ng_filter != 'All':
            filtered = filtered[filtered['neighbourhood_group'] == ng_filter]
        if rt_filter != 'All':
            filtered = filtered[filtered['room_type'] == rt_filter]

        # Leaderboard - review terbaru
        top_latest = filtered.sort_values(by='last_review', ascending=False).head(20).reset_index(drop=True)
        st.markdown("### 🔥 20 Listing dengan Review Terbaru")
        st.dataframe(
            top_latest[['name', 'neighbourhood_group', 'room_type', 'price', 'last_review']]
            .style.format({'price': '${:,.0f}'})
            .highlight_max(axis=0, color='lightgreen'),
            use_container_width=True)

        # Bar Race: Tren Review dari waktu ke waktu
        st.markdown("---")
        st.subheader("🏁 Tren Jumlah Review per Wilayah")

        # Tambahkan kolom bulan dari tanggal review
        filtered['review_month'] = filtered['last_review'].dt.to_period('M').astype(str)

        # Hitung jumlah review per bulan dan neighbourhood_group
        trend = (
            filtered.groupby(['review_month', 'neighbourhood_group'])
            .size()
            .reset_index(name='total_review'))

        # Buat animasi bar race
        if not trend.empty:
            fig = px.bar(
                trend,
                x='total_review',
                y='neighbourhood_group',
                color='neighbourhood_group',
                animation_frame='review_month',
                orientation='h',
                range_x=[0, trend['total_review'].max() * 1.1],
                title="📊 Jumlah Review Tiap Bulan per Wilayah",
                color_discrete_sequence=px.colors.qualitative.Set2,
                height=500)
            
            fig.update_layout(yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Data tidak tersedia untuk animasi tren. Coba hilangkan filter.")
