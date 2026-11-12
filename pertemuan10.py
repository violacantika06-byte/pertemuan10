import pandas as pd
import streamlit as st
import plotly.express as px
import yfinance as yf
from datetime import date

st.title("pertemuan 10: interaksi streamlit dan yahoo finance")

kamus_ticker = {
    "GOOGL": 'Google',
    'AAPL': 'Apple Inc',
    'SBUX' : 'starbucks',
    'MCD': "McDonal's Corp",
    'META': "Meta Platform Inc",
    'TLKM.JK': "Telkom Indonesia (Persero) Tbk PT",
    'BBNI.JK': 'Bank Negara Indonesia (Persero) Tbk PT',
    'BMRI.JK': 'Bank Mandiri (Persero) Tbk PT',
    'BBRI.JK': 'Bank Rakyat Indonesia (Persero) Tbk PT',
    'NESN': 'Nestle SA'
}

ticker_symbol = st.selectbox(
    'Silahkan pilih kode perusahaan:',
    sorted(kamus_ticker.keys())
)

st.write(kamus_ticker[ticker_symbol])

Ticker_data = yf.Ticker( ticker_symbol )
pilihan_periode = st.selectbox(
    'pilih periode:',
    ['1d','5d', '1mo', '3mo', '6mo', '3y', '2y']
)
tgl_mulai = st.date_input(
    'muali tanggal',
    value=date.today()
)
tgl_akhir = st.date_input(
    'sampai tanggal',
    value=date.today()
)
st.write(f'tgl_mulai: {tgl_mulai}')
st.write(f'tgl_akhir: {tgl_akhir}')

df_Ticker = Ticker_data.history(
    start=str(tgl_mulai),
    end=str(tgl_akhir)
)

pilihan_tampil_tabel = st.checkbox('tampilkan tabel')

if pilihan_tampil_tabel == True:
    st.write("#### lima data awal")
    st.write(df_Ticker.head())

st.write(f"## visualisasi pergerakan saham {kamus_ticker[ticker_symbol]}")

pilihan_atribut = st.multiselect(
    'silahkan pilih atribut yang akan ditampilkan:',
    ['Low', 'High', 'Open', 'Close', 'Volume']
)
grafik= px.line(
    df_Ticker,
    y=pilihan_atribut,
    title=f"harge saham {kamus_ticker[ticker_symbol]}"
)
st.plotly_chart( grafik )
st.write()

