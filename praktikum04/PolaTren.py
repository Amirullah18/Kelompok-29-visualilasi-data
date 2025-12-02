import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Data jumlah mahasiswa per jurusan (5 tahun terakhir)
data = {
    'Tahun': ['2019', '2020', '2021', '2022', '2023'],
    'Teknik_Komputer': [100, 110, 120, 130, 140],
    'Sistem_Informasi': [130, 125, 135, 165, 166],
    'Teknik_Informatika': [100, 99, 100, 100, 110],
    'Data_Science': [70, 75, 80, 95, 90]
}

# Membuat DataFrame untuk visualisasi
df = pd.DataFrame(data)

# Streamlit UI
st.title("Visualisasi Trend Jumlah Mahasiswa Per Jurusan Komputer (5 Tahun Terakhir)")

# Membuat filter tahun
filter_tahun = st.multiselect("Filter Tahun:", df['Tahun'], default=df['Tahun'])

# Membuat filter jurusan
jurusan_list = ['Teknik_Komputer', 'Sistem_Informasi', 'Teknik_Informatika', 'Data_Science']
filter_jurusan = st.multiselect("Filter Jurusan:", jurusan_list, default=jurusan_list)

# Filter data berdasarkan input pengguna
filtered_data = df[df['Tahun'].isin(filter_tahun)][filter_jurusan + ['Tahun']]

# Menampilkan data tabel
st.subheader("Data Jumlah Mahasiswa")
st.dataframe(filtered_data)

# Membuat Bar Chart dengan filter
st.subheader("Bar Chart dengan Filter")
fig, ax = plt.subplots(figsize=(10, 6))

# Membuat Bar Chart berdasarkan data yang difilter
x = range(len(filtered_data['Tahun']))
width = 0.2

for i, jur in enumerate(filter_jurusan):
    ax.bar([p + i * width for p in x], filtered_data[jur], width=width, label=jur)

# Mengatur sumbu dan judul
ax.set_title("Jumlah Mahasiswa per Jurusan (Berdasarkan Filter)")
ax.set_xlabel("Tahun")
ax.set_ylabel("Jumlah Mahasiswa")
ax.set_xticks([p + width * (len(filter_jurusan) - 1) / 2 for p in x])
ax.set_xticklabels(filtered_data['Tahun'])
ax.legend()

# Menampilkan plot di Streamlit
st.pyplot(fig)