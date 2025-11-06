# import library yang dibutuhkan
import streamlit as st

# text element
# header - untuk membuat tulisan header
st.header("Ini header")
st.subheader("Ini sub Header")
st.text("Ini text biasa tanpa format")
st.markdown("**ini text bold** dan *ini text italic") # markdwon untuk memformat text tebal/miring
st.markdown("""
- ini baris 1
- ini menggunakan markdwon multibaris
1. ini baris 2
2. ini menggunakan markdown multibaris
* ini baris 3
* ini menggunakan markdown multibaris
""")
st.caption("Ini caption") # text kecil dibawah elemen (untuk penjelasana)
st.title("Visualisasi Data")

# coba mandiri
# tuliskan
# 1. judul praktikum pakai title()
# 2. bagian praktikum pakai subheader()
# 3. nama lengkap anggota - nim pakai markdown multibaris """"

# bagian 2: menampilkan Rumus (laTex)
st.header("Displaying LaTex")
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''') # rumus trigonometri
st.latex(r''' (a+b)^2 + b^2 + 2ab ''') # rumus kuadrat binominal

# bagian 3: Menampilkan kode program
st. header("Displaying Code")
st.subheader("Python Code")

# simpan ke variable
code = ''' 
def hello():    
    print("Hello, Streamlit!)
'''

# st.code() untuk menampilkan potongan kode dengan format rapih dan syntax highlighting
st.code(code, language='python')

st.subheader("Java code")
st.code(""" 
public class GFG {
        public static void main(String arg[]) {
            system.out.printIn(Hello World!);
        }
     }
""", language='java')
# Fungsi st.code() bisa digunakan untuk bahasa pemrograman lain seperti java, javaScript, C++, HTML, dll

st.subheader("javaScript Code")
st.code(""" 
<script>
try {
    addalert("Welcome guest!); // kesalahan ketik (addalaert)
    sengaja dibuat untuk menimbulkan error
}
catch(err) {
    document.getElementById("demo").innerHTML = err.message; //
    Menampilkan pesan error di elemen HTML dengan id 'demo'
}
 dijalankan """, language='Javascript')
# kode ini menunjukan contoh bagimana mengenai error (exception) di javaScript.
# Hasilnya tidak dijalankan di streamlit tapi ditampilakn sebagai contoh kode,