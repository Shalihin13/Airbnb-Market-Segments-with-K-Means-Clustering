import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Airbnb Segment",
    page_icon="🏰",
    layout="wide",
    initial_sidebar_state="collapsed")

# Header
st.markdown("""
    <h1 style='text-align: center; color: #FF5A5F; font-size: 45px;'>🏰 Airbnb Market Segmentation</h1>
    <p style='text-align: center; font-size: 18px; color: gray;'>
     Discover insights, visualize trends, and explore customer clusters</p>""",unsafe_allow_html=True)

# Tabs horizontal
tab1, tab2, tab3 = st.tabs(["📌**Introduction**", "📊 **Visualization**", "📈 **Clustering**"])

with tab1:
    with st.spinner("Loading Introduction..."):
        import Introduction
        Introduction.view_intro()

with tab2:
    with st.spinner("Loading Visualizations..."):
        import visual
        visual.view_project()

with tab3:
    with st.spinner("Running Clustering Model..."):
        import cluster
        cluster.predict()
