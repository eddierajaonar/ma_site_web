import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
import mplfinance as fplt

@st.cache
def get_data(url):
    data = pd.read_csv(url)
    tickers = data['Symbol'].tolist()
    return tickers

def compare(df):
    rel = df.pct_change()
    cumulative = (1+rel).cumprod() -1
    cumulative = cumulative.fillna(0)
    return cumulative



def finance_dashboard():
    url = 'https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents.csv'
    
    tickers = get_data(url)
    
    st.markdown("""<h1 style="color:blue;">Finance Dashboard</h1>""", unsafe_allow_html=True)
    
    dropdown = st.multiselect('symbole S&P500 à comparer:', tickers)
    
    start = st.date_input('Date de debut:', value=pd.to_datetime('2021-01-01'))
    end = st.date_input('Date de fin:', value=pd.to_datetime('today'))
    
    if len(dropdown) > 0:
        #df = yf.download(dropdown, start, end)['Adj Close']
        df = compare(yf.download(dropdown, start, end)['Adj Close'])
        st.markdown('---')
        ma_string = ' '.join(dropdown)
        st.subheader(f'Comparaison : {ma_string}')
        st.line_chart(df)
        
    
if __name__ == "__main__":
    finance_dashboard()