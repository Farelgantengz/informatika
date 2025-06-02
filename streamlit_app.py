import streamlit as st

st.title("lagi makan ayam geprek")
st.write(
    "AKHIRNYA BISA BIKIN AKUNNNN"
)
st.image("mantaprek.png")
st.header("Pengecek Nilai Genap/Ganjil")
angka = st.number_input("Masukkan Angka:", value=0, step=1)

if (angka %2) == 0:
    st.write(f"{angka} itu Bilangan Genap cuyy")
else:
    st.write(f"{angka} itu Bilangan Ganjil cuyy")
