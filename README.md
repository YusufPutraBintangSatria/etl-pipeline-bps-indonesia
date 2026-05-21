# Indonesian Socio-Economic Data Pipeline & Dashboard (BPS 2021)

An end-to-end Data Engineering mini-project that extracts socio-economic data from the Central Bureau of Statistics (BPS) Indonesia for the year 2021, processes it through a robust ETL pipeline, and visualizes the insights using an interactive web dashboard.

---

## 📌 Latar Belakang & Masalah (Problem Statement)
Data sosial-ekonomi pemerintah seringkali menjadi landasan dalam pengambilan keputusan dan kebijakan publik. Namun, data mentah (*raw data*) yang diunduh dari portal publik seringkali memiliki kendala:
1. **Inkonsistensi Format:** Format penulisan angka, desimal, dan ribuan yang tidak standar antar wilayah.
2. **Data Kotor:** Adanya nilai kosong (*missing values*) atau penamaan kolom yang tidak ramah *database*.
Jika data ini langsung divisualisasikan tanpa proses pembersihan, akan menghasilkan kesimpulan yang fatal dan menyesatkan (contoh: wilayah dengan ekonomi kecil terlihat lebih besar dari ibu kota karena kesalahan pembacaan desimal oleh sistem).

## 🎯 Tujuan Proyek (Objectives)
1. Membangun *pipeline* otomatis (ETL) untuk mengekstrak, membersihkan, dan menormalisasi data mentah pemerintah.
2. Menyelesaikan anomali inkonsistensi format data numerik menggunakan manipulasi teks dan Pandas.
3. Menyediakan *database* relasional yang bersih (*clean data*) dan siap digunakan untuk analisis lanjutan.
4. Membangun *dashboard* interaktif sebagai simulasi penyajian data untuk pimpinan/eksekutif.

## 📂 Sumber Dataset (Data Source)
* **Sumber Data:** Badan Pusat Statistik (BPS) Indonesia / Kaggle (diunggah oleh Danny Theodore).
* **Tahun Data:** 2021 (Data *Cross-Sectional*).
* **Link Dataset:** [Socio-Economic of Indonesia in 2021](https://www.kaggle.com/datasets/dannytheodore/socio-economic-of-indonesia-in-2021)

---

## ⚙️ Tech Stack & Architecture
* **Language:** Python 3.x
* **Data Manipulation:** Pandas
* **Database Layer:** SQLite (SQL Storage)
* **Visualization Engine:** Streamlit
* **Deployment Ready:** Clean and modular script structure

---

## 🛠️ Data Pipeline Architecture (ETL)

### 1. Extract
* Membaca data mentah dari file `data_bps_2021.csv` yang berisi metrik sosial-ekonomi seluruh kabupaten dan kota di Indonesia.

### 2. Transform (Data Cleansing & Anomaly Resolution)
Tahap ini merupakan *core logic* penting untuk memastikan integritas data sebelum dianalisis. Proyek ini berhasil mengidentifikasi dan menangani **anomali data kritis**:
* **Temuan Anomali:** Ketidakkonsistenan penulisan format numerik pada kolom PDRB (*Regional GDP*). Wilayah metropolitan besar ditulis dengan format desimal (contoh Jakarta Pusat ditulis `701.98`), sedangkan wilayah kecil ditulis bulat (contoh Manokwari Selatan ditulis `819`).
* **Solusi Cleansing:** Ditambahkan manipulasi string berbasis Pandas untuk menormalisasi teks, menghapus titik desimal palsu, dan mengembalikan tipe data ke bentuk numerik murni (`float`). 
* **Standardisasi:** Mengubah nama kolom menjadi format *snake_case* standard database, serta menangani *missing values* menggunakan metode *imputation*.

### 3. Load
* Menyimpan data yang telah bersih dan tervalidasi ke dalam database SQLite (`database_bps.db`) dengan nama tabel `tabel_ekonomi`.

---

## 📊 Dashboard Features
Dashboard interaktif dibangun menggunakan library **Streamlit** untuk memfasilitasi pengguna dalam melakukan *deep dive* analysis:
1. **Key Performance Indicators (KPIs):** Menampilkan metrik agregat nasional.
2. **Top 10 PDRB (Ekonomi) Nasional:** Visualisasi interaktif menggunakan Bar Chart untuk melihat wilayah dengan kontribusi ekonomi terbesar **setelah** proses *cleansing*.
3. **Top 10 Persentase Penduduk Miskin:** Mengidentifikasi wilayah dengan tingkat ketimpangan sosial tertinggi.
4. **Data Explorer Table:** Fitur pencarian dan filter tabel data mentah secara dinamis.

<img width="1918" height="1078" alt="1" src="https://github.com/user-attachments/assets/0f4d58ff-1fed-41d6-9ac9-1cf3ff9501a8" />


---

Execution Steps
Jalankan Pipeline ETL:
Buka file Jupyter Notebook dan jalankan semua sel (Run All) untuk mengekstrak data mentah, membersihkan anomali PDRB, dan menyimpannya ke database SQLite lokal secara otomatis.

```
Bash
DE2.ipynb
```
Jalankan Web Dashboard:
Setelah proses ETL selesai, jalankan dashboard interaktif dengan perintah:
```
Bash
streamlit run app_dashboard.py
```

📝 Key Learnings (Studi Kasus Wawancara)
Proyek ini membuktikan pemahaman mendalam terhadap siklus data:

- Tidak hanya sekadar menampilkan grafik, melainkan mampu melakukan sanity check terhadap data.

Sebelum Data Cleansing (Anomali Format Desimal):

<img width="1507" height="893" alt="2" src="https://github.com/user-attachments/assets/1052249b-3d14-4648-b825-08b378034f27" />


- Memahami bahwa Data Engineering yang kuat (proses Transform) sangat krusial agar produk akhir tidak menyajikan informasi yang menyesatkan (Garbage In, Garbage Out).
