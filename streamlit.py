import streamlit as st
import numpy as  np
import pandas as pd

#Menambahka judul 
st.title("Aplikasi Dasar dengan Streamlit")
st.title("Aplikasi Dasar dengan Streamlit")

#Menambahkan Penjelasan
st.write("Ini adalah aplikasi pertama yang menggunakan streamlit!")

#Membuat Dataframe
data ={
    'Nama': ['Hilma', 'aya', 'tari', 'malika', 'galuh'],
    'Usia': [19, 20, 23, 18,21],
    'Kota': ['Makassar', 'Takalar', 'Sidrap', 'Jeneponto', 'Ngawi']
}
df=pd.DataFrame(data)

#Menampilkan DataFrame
st.write(df)

#3.1 Elemen Text
import streamlit as st
st.title('Selamat Datang di Aplikasi Streamlit')
st.header('Bagian 1: Algoritma dan Pemrograman')
st.subheader('Subbagian 1: Streamlit')
st.caption('Data ini hanya untuk tujuan demonstrasi tugas')
st.code('import pandas as pd')
st.text('ini adalah teks biasa tanpa format dan penekanan.')
st.latex(r' y = mx + b')
st.markdown('**Saya sedih** tapi _baik baik saja_ serta [Tautan](https://streamlit.io)')
st.divider()

#4.Menampilkan Data
#a.API

import streamlit as st
import requests
import pandas as pd

st.title('Data dari API')

url = 'https://jsonplaceholder.typicode.com/users'  #API contoh
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.dataframe(df)
    print(data)
else:
    st.error('Gagal mengambil data dari API')

#b. Menampilkan Data dari File(CSV,Excel,dll.)

uploaded_file = st.file_uploader("Pilih file CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
else:
    st.write("Tidak ada file yang diunggah")

#c. Menggunakan st.write()

#Data sederhanah
data = {
    'Nama': ['Nurul', 'Adnia', 'Hilma'],
    'Umur': [28, 25, 20],
    'Kota': ['Makassar', 'Bandung', 'Gowa']
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menampilkan DataFrame
st.write("Tabel Data:")
st.write(df)

#D. Menggunakan DataFrame random
df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

# Menampilkan DataFrame di Streamlit
st.dataframe(df)

#5. File Metric

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Omset", value="Rp 200 Juta", delta="+5%")
with col2:
    st.metric(label="User Aktif", value="1.250", delta="+2%")
with col3:
    st.metric(label="Refund", value="15", delta="-1%")

col1, col2, = st.columns(2)

#6. Menampilkan Grafik
#6.1 Line Chart-st.line_chart()

import streamlit as st
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(data)

##6.2 Bar Chart-st.bar_chart()

st.bar_chart(data)

##6.3 Altair Chart_st.altair_chart()

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
)

chart = alt.Chart(data.reset_index()).mark_line().encode(
    x='index',
    y='a'
)

st.altair_chart(chart, use_container_width=True)

##6.4 Map-st.map()
df = pd.DataFrame(
    np.random.randn(1000, 2)/[50, 50]+[37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(df)

#7. Input Form
import streamlit as st

with st.form("form_input"):
    nama = st.text_input("Nama")
    alamat = st.text_area("Alamat")
    usia = st.number_input("Usia", min_value=0)
    tanggal_lahir = st.date_input("Tanggal Lahir")
    waktu_janji = st.time_input("Waktu Janjian")
    jenis_kelamin = st.radio("Jenis Kelamin", ("Pria", "Wanita"))
    hobi = st.multiselect("Hobi", ["Membaca", "Olahraga", "Musik", "Traveling"])
    warna_favorit = st.color_picker("Pilih warna favorit")
    file_foto = st.file_uploader("Upload Foto")
    foto_kamera = st.camera_input("Ambil Foto dari Kamera")
    rating = st.slider("Rating Kepuasan", 1, 10)

    submitted = st.form_submit_button("Kirim Data")

if submitted:
    st.success(f"Data {nama} berhasil dikirim!")

#8. Menampilkan Media
##8.1 Menampilkan gambar

import streamlit as st
from PIL import Image

image = Image.open('fotoku.jpeg')
st.image(image, caption='Foto Saya')

st.image('https://cdn.sulselsatu.com/imageresize/assets/media/upload/2025/04/WhatsApp-image-2025-04-27-at.16.25.16.jpeg&width=200&height=112', caption='Gambar dari' \
'URL', use_column_width=True)

## 8.2 Menampilkan Video
# Menampilkan video dari URL (misalnya YouTube)
st.video('https://www.youtube.com/watch?v=9zctVgA2ZkY')

# Menampilkan HTML
import streamlit as st

# Menampilkan HTML langsung
html_code = """
<h1>Selamat datang di Aplikasi Streamlit!</h1>
<p>Ini adalah <strong>paragraf</strong> HTML yang dapat diproses oleh Streamlit.</p>
"""
st.markdown(html_code, unsafe_allow_html=True)

#Contoh: Menggunakan Kolom untuk Menampilkan Elemen Secara Berdampingan
import streamlit as st

# Membuat dua kolom
col1, col2 = st.columns(2)

# Menampilkan konten di kolom pertama
with col1:
    st.header("Kolom 1")
    st.write("Ini adalah konten di kolom pertama.")
    st.button("Tombol Kolom 1")

# Menampilkan konten di kolom kedua
with col2:
    st.header("Kolom 2")
    st.write("Ini adalah konten di kolom kedua.")
    st.button("Tombol Kolom 2")

#Menggunakan st.expander() untuk Konten yang Bisa Dilipat
import streamlit as st

with st.expander("Klik untuk melihat lebih banyak"):
    st.write("Ini adalah konten tersembunyi yang bisa dilihat saat pengguna klik expander.")
    st.image("https://via.placeholder.com/150", caption="Contoh Gambar")

#Layout Menggunakan st.container()
import streamlit as st

# Membuat container
container = st.container()

# Menambahkan elemen ke dalam container
with container:
    st.header("Konten di dalam Container")
    st.write("Ini adalah elemen-elemen yang ada dalam container.")
    st.button("Tombol dalam Container")

#Menggunakan Sidebar
import streamlit as st

# Menambahkan elemen ke Sidebar
st.sidebar.header("Ini Sidebar")
st.sidebar.radio("Pilih Opsi", ["Opsi 1", "Opsi 2", "Opsi 3"])

# Konten utama
st.title("Konten Utama")
st.write("Ini adalah konten utama yang ditampilkan di layar.")