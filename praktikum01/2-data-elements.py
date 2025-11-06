# import library
import streamlit as st
import pandas as pd         # untuk mengelola data dalam bentuk tabel (dataframe)
import numpy as np          # untuk membuat data numerik acak
import altair as alt        # untuk membuuat chart interaktif

# Menampilkan judul dan deskripsi
st.title("Praktikum 1 - Visualisasi Data")          # Menampilkan judul utama di halaman
st.caption("Bagian 2: Data Elements")               # Menampilkan keterangan bagian

# st.markdown digunakan untuk menampilkan teks dengan format Markdown (bullet list, bold, italic, dll.)
st.markdown("""
Kelompok 29
1. Amirullah - 0110222106
2. Indah Agustin - 0110222250
3. Miftahul Jannah - 0110222101
""")


# DataFrame : struktur data berbentuk tabel (baris dan kolom) yang disediakan oleh library pandas
st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
    )


# menampilkan dataFrame
st.dataframe(df)

# Highlinght Nilai Minumun
st.subheader("Highlinght Minimun Value di DataFrame")

# Highlight nilai terkecil disetiap kolom dataframe
# axis=0 bekerja per kolom
st.dataframe(df.style.highlight_min(axis=0))

# tabel Statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range(10))
    )
# Menampilkan tabel statis
st.table(df)

# Metrics: komponen tampilan angka peting
st.subheader("Metrics")
# Menampilkan metrik tunggal (nilai utama + perubahan nilai)
st.metric(label="Temperature", value="31 °C", delta="1.2 °C") # Kenaikan 1.2 °C

# Metric sesuai delta_color
# delta_color digunakan untuk memberi warna sesuai arah perubahan:
# - "normal" (default): naik -> hijau, turun -> merah
# - "inverse": kebalikannya (naik -> merah)
# - "off"; tidak menampilkan warna perubahan

# definisikan variabel metrics
col1, col2, col3, = st.columns(3)

#menampilkan indikator data
col1.metric("Curah Hujan", "100 cm", "10 cm") # naik dan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar",
    delta_color="inverse") # naik tapi buruk
col3.metric(label="Pelanggan", value=100, delta=-10,
    delta_color="off") # netral (tidak baik, tidak buruk)

# Menampilkan metrik tambahan dengan nilai kosong atau nol
# karena di setting default
st.metric(label="Speed", value=None, delta=0) # kosong & naik baik
st.metric("Trees", "91456", "-1132649") # penurunan

import streamlit as st
import pandas as pd
import numpy as np
df = pd.DataFrame(
    np.random.randn(30, 10),
    columns=('col_no %d' % i for i in range(10)))
# defining multiple arguments in write function
st.write('Here is our Data', df, 'Data is in dataframe format.\n', "\nWrite is Super function")

# importing Necessary Libraries
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st

# Defining random Values for Chart
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['a', 'b'])
# Defining Chart
chart = alt.Chart(df).mark_bar().encode(
    x='a', y='b', tooltip=['a', 'b'])

# Defining Chart in write() function
st.write(chart)

# Math calculations with no functions defined
"Adding 5 & 4 =", 5+4

# Displaying Variable 'a' and its value
a = 5
'a', a

# Markdown with Magic
"""
# Magic Feature
Markdown working without defining its function explicitly.
"""

# Dataframe using magic
import pandas as pd
df = pd.DataFrame({'col': [1,2]})
'dataframe', df

# Magic working on Charts
import matplotlib.pyplot as plt
import numpy as np
s = np.random.logistic(10, 5, size=5)
chart, ax = plt.subplots()
ax.hist(s, bins=15)
# Magic chart
"chart", chart