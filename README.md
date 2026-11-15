# Bike Sharing Analysis Dashboard

## Deskripsi
Project ini merupakan analisis data penyewaan sepeda menggunakan Bike Sharing Dataset periode 2011–2012. Analisis dilakukan untuk mengetahui pola penyewaan berdasarkan waktu dan kondisi cuaca.

## Struktur Folder
- `dashboard/`: Berisi file aplikasi dashboard.
- `data/`: Berisi dataset day.csv dan hour.csv.
- `Proyek_Analisis_Data.ipynb`: Notebook analisis data.
- `requirements.txt`: Daftar library yang dibutuhkan.
- `url.txt`: Link dashboard yang telah di-deploy.

## Instalasi Library
Jalankan perintah berikut pada terminal:

```bash
pip install -r requirements.txt
```

## Menjalankan Dashboard
Pastikan terminal berada di folder submission, kemudian jalankan:

```bash
streamlit run dashboard/dashboard.py
```

Dashboard dapat diakses melalui browser pada alamat:

`http://localhost:8501`

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
