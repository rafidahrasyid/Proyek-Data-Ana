import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='white')

#Load Data
monthly_orders_df = pd.read_csv('Dashboard\\monthly_orders.csv')
products_order_df = pd.read_csv('Dashboard\\products_order_df.csv')

#Dashboard
st.title('Brazilian E-commerce Analysis Dashboard')

#Analisis Pertanyaan 1
st.header('Analisis Pertanyaan 1 :Pola pembelian produk dalam setahun pertama')
st.write("Pola pembelian produk setahun pertama.")

fig = plt.figure(figsize=(10,6))
sns.barplot(data=monthly_orders_df, x='Month', y='Number of Orders', hue='Month', palette='Set2', legend=False)
plt.title('Pola Pembelian Setahun Pertama')
plt.xlabel('Bulan')
plt.ylabel('Jumlah Pesanan')
plt.xticks(rotation=40)
st.pyplot(fig)

st.write("Dari visualisasi ini,dapat terlihat bahwa bulan Agustus,May,dan Juli menonjol sebagai bulan dengan volume pembelian produk yang lebih tinggi. Data ini menunjukkan bahwa pada bulan tersebut terjadi lonjakan pesanan yang signifikan dibandingkan bulan lainnya.")
st.write("Perusahaan perlu ecara rutin memonitor stok dan mengelola proses logistik mereka setiap bulan guna memastikan bahwa mereka dapat megantisipasi fluktasi permintaan yang mungkin terjadi.")

#Analisis Pertanyaan 2
st.header('Analisis Pertanyaan 2 : Tren pembelian setiap bulan.')

fig = plt.figure(figsize=(10,5))
sns.lineplot(data=monthly_orders_df, x='Month', y='Number of Orders',marker='o',color='red')
plt.title('Tren Penjualan Bulanan')
plt.xlabel('Month')
plt.ylabel('Jumlah Pesanan')
plt.grid(True)
st.pyplot(fig)

st.write("Berdasarkan data penjualan bulanan, terlihat bahwa bulan Desember dan Februari cenderung memiliki penjualan yang lebih tinggi sedangkan bulan Januari memiliki penjualan yang lebih rendah.")
st.write("Bulan Januari mengalami penjualan yang lebih rendah dikarenakan adanya pajak, biaya transaksi, kenaikan risiko saat perusahaan menerbitkan laporan tahunan. Sedangkan pada bulan Desember dan Februari merupakan bulan yang menjadi musim belanja liburan, sehingga penjualan pada bulan tersebut meningkat.")