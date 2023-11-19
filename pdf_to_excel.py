import pandas as pd
import tabula
import streamlit as st

data = st.file_uploader('PDFファイルをアップロードしてください。')
if data != None:
    dfx = tabula.io.read_pdf(data,lattice=True,pages='all')
    page = st.number_input('変換するページNOを入力してください。',1,len(dfx))
    df = dfx[page-1]

    st.text('PDFをアップロードしてください。')

    df
    csv = df.to_csv().encode('SHIFT-JIS')
        # _dl_file = dfx[page].to_excel('output.xlsx')
    st.download_button(label='Data Download', 
                        data=csv, 
                        file_name='output.csv',
                        mime='text/csv',
                        )