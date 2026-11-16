# Bike Sharing Analytics Dashboard 

## Deskripsi Proyek

Proyek ini merupakan analisis data penyewaan sepeda menggunakan Bike Sharing Dataset periode 2011–2012. Analisis dilakukan untuk mengetahui pola penyewaan sepeda berdasarkan jam dalam sehari dan kondisi cuaca.

Hasil analisis disajikan dalam bentuk dashboard interaktif menggunakan Streamlit untuk membantu memahami pola permintaan penyewaan sepeda.

## Informasi Dataset

Dataset yang digunakan adalah Bike Sharing Dataset yang terdiri dari:

- `day.csv`: Data penyewaan sepeda berdasarkan hari.
- `hour.csv`: Data penyewaan sepeda berdasarkan jam.

Kedua dataset berisi informasi mengenai jumlah penyewaan sepeda, waktu, kondisi cuaca, dan variabel pendukung lainnya.

## Struktur Direktori

```text
bike-sharing-analysis/
├── dashboard/
│   └── dashboard.py
├── data/
│   ├── day.csv
│   └── hour.csv
├── Proyek_Analisis_Data.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

## Persiapan Environment

### 1. Clone Repository

Clone repository dari GitHub menggunakan perintah:

```bash
git clone https://github.com/naylazahira/bike-sharing-analysis.git
```

Masuk ke direktori utama proyek:

```bash
cd bike-sharing-analysis
```

Pastikan terminal berada di direktori utama proyek, yaitu folder yang berisi file `requirements.txt`.

### 2. Membuat Virtual Environment

Buat virtual environment agar dependensi proyek terisolasi dari Python environment lainnya.

```bash
python -m venv .venv
```

### 3. Mengaktifkan Virtual Environment

Windows (Command Prompt):

```bash
.venv\Scripts\activate
```

Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 4. Instalasi Dependensi

Setelah virtual environment aktif, pastikan terminal berada di direktori utama proyek yang memiliki file `requirements.txt`.

Jalankan perintah berikut:

```bash
pip install -r requirements.txt
```

Dependensi yang digunakan dalam proyek ini meliputi:

- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Menjalankan Dashboard

Pastikan virtual environment sudah aktif dan seluruh dependensi berhasil diinstal.

Jalankan aplikasi menggunakan perintah berikut dari direktori utama proyek:

```bash
streamlit run dashboard/dashboard.py
```

Setelah aplikasi berhasil dijalankan, dashboard dapat diakses melalui browser pada alamat:

```text
http://localhost:8501
```

## Fitur Dashboard

Dashboard menyediakan beberapa fitur analisis, yaitu:

1. Filter data berdasarkan tahun.
2. Filter data berdasarkan kondisi cuaca.
3. Menampilkan total penyewaan sepeda.
4. Menampilkan rata-rata penyewaan sepeda per hari.
5. Menampilkan jam dengan tingkat penyewaan tertinggi.
6. Visualisasi pola penyewaan berdasarkan jam.
7. Visualisasi penyewaan berdasarkan kondisi cuaca.
8. Visualisasi penyewaan berdasarkan kategori waktu.

## Pengujian Aplikasi

Untuk memastikan dashboard berjalan dengan baik, lakukan langkah berikut:

1. Aktifkan virtual environment.
2. Instal seluruh dependensi menggunakan `requirements.txt`.
3. Jalankan dashboard menggunakan perintah Streamlit.
4. Pastikan dashboard berhasil terbuka melalui browser.
5. Coba ubah filter tahun dan kondisi cuaca.
6. Pastikan ringkasan dan visualisasi dapat ditampilkan sesuai data yang dipilih.

## Teknologi yang Digunakan

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

## Link Dashboard

Link dashboard hasil deployment dapat dilihat pada file `url.txt` di direktori utama proyek.
