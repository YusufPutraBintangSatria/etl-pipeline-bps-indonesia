import sqlite3
import pandas as pd
import streamlit as st

# ==========================================
# 1. KONFIGURASI HALAMAN DASHBOARD
# ==========================================
st.set_page_config(
    page_title="Dashboard Ekonomi & Demografi BPS", 
    page_icon="📈", 
    layout="wide"
)

# ==========================================
# 2. FUNGSI UNTUK MENGAMBIL DATA DARI DATABASE
# ==========================================
def ambil_data_db():
    # Konek ke database SQLite yang barusan lu bikin
    conn = sqlite3.connect("database_bps.db")
    query = "SELECT * FROM tabel_ekonomi"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

df = ambil_data_db()

# ==========================================
# 3. HEADER & JUDUL
# ==========================================
st.title("📈 Dashboard Socio-Economic Indonesia (Data BPS 2021)")
st.markdown("Visualisasi data hasil pipeline ETL dari dataset resmi Badan Pusat Statistik (BPS). Menampilkan indikator ekonomi dan demografi per provinsi/kabupaten.")
st.markdown("---")

# ==========================================
# 4. SIDEBAR KONTROL / FILTER
# ==========================================
st.sidebar.header("🎛️ Filter Wilayah")
# Bikin dropdown otomatis berdasarkan nama provinsi di database
list_provinsi = ["Semua Provinsi"] + sorted(list(df["provinsi"].unique()))
pilihan_provinsi = st.sidebar.selectbox("Pilih Provinsi:", list_provinsi)

# LOGIKA FILTER DATA
if pilihan_provinsi != "Semua Provinsi":
    df_filtered = df[df["provinsi"] == pilihan_provinsi]
else:
    df_filtered = df.copy()

# ==========================================
# 5. MENAMPILKAN KPI (Key Performance Indicator)
# ==========================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    avg_miskin = df_filtered["persentase_miskin"].mean()
    st.metric(label="Rata-rata Kemiskinan (%)", value=f"{avg_miskin:.2f} %")

with col2:
    total_pdrb = df_filtered["pdrb"].sum()
    st.metric(label="Total PDRB Ekonomi", value=f"{total_pdrb:,.1f}")

with col3:
    avg_harapan_hidup = df_filtered["harapan_hidup"].mean()
    st.metric(label="Harapan Hidup", value=f"{avg_harapan_hidup:.1f} Tahun")

with col4:
    avg_sekolah = df_filtered["rata_rata_sekolah"].mean()
    st.metric(label="Rata-rata Lama Sekolah", value=f"{avg_sekolah:.1f} Tahun")

st.markdown("---")

# ==========================================
# 6. VISUALISASI GRAFIK
# ==========================================
if pilihan_provinsi == "Semua Provinsi":
    st.info("💡 Pilih salah satu provinsi di sidebar kiri untuk melihat perbandingan antar Kabupaten/Kota secara detail.")
    
    # Menampilkan Top 10 Nasional jika belum difilter
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        st.subheader("🏆 Top 10 Kab/Kota: PDRB (Ekonomi) Tertinggi")
        top_pdrb = df_filtered.sort_values(by="pdrb", ascending=False).head(10)
        st.bar_chart(data=top_pdrb.set_index("kabupaten_kota")["pdrb"])
        
    with col_chart2:
        st.subheader("🚨 Top 10 Kab/Kota: Persentase Kemiskinan Tertinggi")
        top_miskin = df_filtered.sort_values(by="persentase_miskin", ascending=False).head(10)
        st.bar_chart(data=top_miskin.set_index("kabupaten_kota")["persentase_miskin"])

else:
    # Menampilkan data Kabupaten/Kota sesuai provinsi yang dipilih
    col_chart1, col_chart2 = st.columns(2)
    with col_chart1:
        st.subheader(f"📈 PDRB per Kabupaten/Kota di {pilihan_provinsi}")
        st.bar_chart(data=df_filtered.set_index("kabupaten_kota")["pdrb"])
        
    with col_chart2:
        st.subheader(f"📊 Persentase Kemiskinan di {pilihan_provinsi}")
        st.bar_chart(data=df_filtered.set_index("kabupaten_kota")["persentase_miskin"])

st.markdown("---")

# ==========================================
# 7. MENAMPILKAN TABEL DATA BERSIH
# ==========================================
st.subheader("📋 Rincian Data Demografi & Ekonomi")
st.dataframe(df_filtered, use_container_width=True)

st.caption("Project Data Engineering & Dashboard | Tech Stack: Python, Pandas, SQLite, Streamlit")