
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Konfigurasi halaman
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

# Membaca dataset
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

hour_df = pd.read_csv(DATA_DIR / "hour.csv")
day_df = pd.read_csv(DATA_DIR / "day.csv")

# Mengubah tipe data tanggal
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Konfigurasi visualisasi
sns.set_theme(style="whitegrid")

# Judul dashboard
st.title("Bike Sharing Analytics Dashboard")
st.markdown(
    "Dashboard analisis pola penyewaan sepeda berdasarkan "
    "waktu dan kondisi cuaca selama periode 2011–2012."
)

st.divider()

# Sidebar untuk filter
st.sidebar.header("Filter Dashboard")

selected_year = st.sidebar.selectbox(
    "Pilih Tahun",
    options=[0, 1],
    format_func=lambda x: "2011" if x == 0 else "2012"
)

weather_options = {
    "Semua Cuaca": None,
    "Cerah / Sedikit Berawan": 1,
    "Berkabut / Berawan": 2,
    "Hujan Ringan / Salju Ringan": 3,
    "Hujan Lebat / Salju Lebat": 4
}

selected_weather = st.sidebar.selectbox(
    "Pilih Kondisi Cuaca",
    options=list(weather_options.keys())
)

# Filter data berdasarkan tahun
filtered_hour = hour_df[hour_df['yr'] == selected_year].copy()
filtered_day = day_df[day_df['yr'] == selected_year].copy()

# Filter cuaca untuk analisis per jam
weather_code = weather_options[selected_weather]

if weather_code is not None:
    filtered_hour = filtered_hour[
        filtered_hour['weathersit'] == weather_code
    ]

# Menghitung KPI
total_rentals = filtered_day['cnt'].sum()

average_rentals = filtered_day['cnt'].mean()

hourly_average = filtered_hour.groupby('hr')['cnt'].mean()

if not hourly_average.empty:
    peak_hour = int(hourly_average.idxmax())
else:
    peak_hour = None

# Menampilkan KPI
st.subheader("Ringkasan Penyewaan")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Penyewaan",
    f"{total_rentals:,.0f}"
)

col2.metric(
    "Rata-rata Penyewaan / Hari",
    f"{average_rentals:,.0f}"
)

col3.metric(
    "Jam Tersibuk",
    f"{peak_hour:02d}:00" if peak_hour is not None else "-"
)

st.divider()

st.subheader("1. Pola Penyewaan Berdasarkan Jam")

hourly_analysis = filtered_hour.groupby('hr')['cnt'].mean().reset_index()

fig, ax = plt.subplots(figsize=(12, 5))

sns.lineplot(
    data=hourly_analysis,
    x='hr',
    y='cnt',
    marker='o',
    ax=ax
)

ax.set_title("Rata-rata Penyewaan Sepeda Berdasarkan Jam")
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata Penyewaan")
ax.set_xticks(range(24))

st.pyplot(fig)
plt.close(fig)

st.caption(
    "Grafik menunjukkan perubahan rata-rata penyewaan sepeda "
    "berdasarkan jam dalam sehari."
)

st.subheader("2. Penyewaan Berdasarkan Kondisi Cuaca")

weather_analysis = filtered_day.groupby(
    'weathersit'
)['cnt'].mean().reset_index()

weather_labels = {
    1: "Cerah",
    2: "Berkabut / Berawan",
    3: "Hujan Ringan / Salju Ringan"
}

weather_analysis['weather_name'] = (
    weather_analysis['weathersit'].map(weather_labels)
)

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    data=weather_analysis,
    x='weather_name',
    y='cnt',
    ax=ax
)

ax.set_title("Rata-rata Penyewaan Berdasarkan Kondisi Cuaca")
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Rata-rata Penyewaan per Hari")
ax.tick_params(axis='x', rotation=15)

st.pyplot(fig)
plt.close(fig)

st.caption(
    "Grafik membandingkan rata-rata jumlah penyewaan "
    "sepeda pada setiap kondisi cuaca."
)

st.subheader("3. Penyewaan Berdasarkan Kategori Waktu")

# Membuat kategori waktu
filtered_hour['time_category'] = pd.cut(
    filtered_hour['hr'],
    bins=[-1, 5, 10, 15, 23],
    labels=['Dini Hari', 'Pagi', 'Siang', 'Sore-Malam']
)

time_analysis = filtered_hour.groupby(
    'time_category', observed=True
)['cnt'].mean().reset_index()

fig, ax = plt.subplots(figsize=(10, 5))

sns.barplot(
    data=time_analysis,
    x='time_category',
    y='cnt',
    ax=ax
)

ax.set_title("Rata-rata Penyewaan Berdasarkan Kategori Waktu")
ax.set_xlabel("Kategori Waktu")
ax.set_ylabel("Rata-rata Penyewaan")

st.pyplot(fig)
plt.close(fig)

st.caption(
    "Pengelompokan waktu dilakukan untuk mengetahui periode "
    "dengan tingkat permintaan penyewaan tertinggi."
)

st.divider()

st.subheader("Insight Analisis")

if not hourly_average.empty:
    st.write(
        f"Jam dengan rata-rata penyewaan tertinggi adalah "
        f"pukul **{peak_hour:02d}:00**."
    )
else:
    st.write("Tidak terdapat data penyewaan untuk filter yang dipilih.")

if not weather_analysis.empty:
    highest_weather = weather_analysis.loc[
        weather_analysis['cnt'].idxmax()
    ]

    st.write(
        f"Kondisi cuaca dengan rata-rata penyewaan tertinggi "
        f"adalah **{highest_weather['weather_name']}**, "
        f"dengan rata-rata **{highest_weather['cnt']:,.2f}** "
        f"penyewaan per hari."
    )

st.info(
    "Rekomendasi: Pengelola dapat meningkatkan ketersediaan "
    "sepeda pada jam sibuk dan menyesuaikan perencanaan "
    "operasional berdasarkan kondisi cuaca."
)

st.caption("Bike Sharing Analytics Dashboard | Data 2011–2012")
