import pandas as pd
import tabula
import streamlit as st

data = st.file_uploader('PDFファイルをアップロードしてください。')
dfx = tabula.read_pdf('sample_pdf.pdf',lattice=True,pages='all')
page = st.number_input('変換するページNOを入力してください。',1,len(dfx))
df = dfx[page-1]
df
csv = df.to_csv().encode('SHIFT-JIS')
# _dl_file = dfx[page].to_excel('output.xlsx')
st.download_button(label='Data Download', 
                   data=csv, 
                   file_name='output.csv',
                   mime='text/csv',
                   )