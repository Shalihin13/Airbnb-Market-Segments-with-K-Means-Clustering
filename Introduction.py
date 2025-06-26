import streamlit as st

def view_intro():
    
    # Judul 
    st.markdown("""
        <div style='text-align: left; padding-top: 10px;'>
            <h1 style='color:Grey;'>🏠 Background </h1>
        </div>""", unsafe_allow_html=True)

    # Panel
    with st.expander("ℹ️ **About Project**", expanded=True):
        st.markdown("""
        **Clustering Market** adalah metode untuk mengelompokkan listing berdasarkan kemiripan fitur, membantu Airbnb memahami preferensi pelanggan & tren pasar.

        **🌐 About Airbnb:**  
        Airbnb.com adalah platform global untuk penyewaan jangka pendek yang menghubungkan tuan rumah dan tamu secara langsung.  
        Seiring dengan meningkatnya persaingan dan kebutuhan personalisasi, sangat penting untuk memahami berbagai segmen listing di dalam platform ini.

        Dengan bantuan teknik **machine learning**, seperti _KMeans Clustering_, kita dapat:
        - Mengenali pola tersembunyi dari data
        - Membagi listing menjadi beberapa segmen pasar
        - Menyusun strategi harga, ketersediaan, dan layanan yang lebih efektif""")

    # Penjelasan cara kerja
    st.markdown("""
    ### 🚀 How Does it Work ❓
    1. Pilih fitur yang ingin dianalisis (misalnya harga, ulasan, jenis kamar)
    2. Model akan mempelajari pola dan karakteristik dari data tersebut
    3. Sistem akan menampilkan hasil klasterisasi berdasarkan kesamaan antar listing
    
    🔍 Hasilnya bisa digunakan untuk:
    - Menentukan target pasar
    - Menyesuaikan strategi bisnis
    - Mengoptimalkan performa listing Airbnb
    """)

    # CTA atau penutup
    st.markdown("""
    <div style='margin-top: 20px; font-size: 16px; color: grey;'>
        Jelajahi tab <b>Visualization</b> untuk mengeksplore data, atau ke tab <b>Clustering</b> untuk mencoba modelnya! Good Luck🧑
    </div>
    """, unsafe_allow_html=True)
