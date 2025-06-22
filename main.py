import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt


st.markdown("""
    <style>
    .title {
        font-size:40px !important;
        color: green;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">Stock Price (NSE)</h1>', unsafe_allow_html=True)


df = pd.read_csv("C:/Users/SRIJITH SHAIBU/OneDrive/Desktop/SRIJITH LEGEND/Projects/Stock Price/nse_stock_list.csv")
df.columns = df.columns.str.strip()
df = df[['SYMBOL']]  
stocks = sorted(df["SYMBOL"].tolist())


with st.form(key="search_btn",border=False):
    choice = st.selectbox("", options=stocks, placeholder="Search Stocks")
    op = st.form_submit_button('Search')
    if op:
        st.balloons()
    st.divider()

with st.container(key='info_data'):
    
    if op and choice:
            st.subheader(f'{choice}')
            sym = choice + ".NS"
            data = yf.Ticker(sym)
            
            
            graph = data.history(period="max", interval="1mo")
            st.line_chart(graph[['Close']])


            col1, sp1, col2, sp2, col3, sp3, col4 = st.columns([4,1,4,1,4,1,4])

            with col1:
                st.write("Symbol:", data.info.get('symbol', 'N/A'))
                st.write("Country:", data.info.get('country', 'N/A'))
                st.write("Sector:", data.info.get('sector', 'N/A'))
                st.write("Previous Close:", data.info.get('previousClose', 'N/A'))
                st.write("Open:", data.info.get('open', 'N/A'))
                st.write("Day Low:", data.info.get('dayLow', 'N/A'))
                st.write("Total Revenue:", data.info.get('totalRevenue', 'N/A'))
                st.write("Debt to Equity:", data.info.get('debtToEquity', 'N/A'))

            with col2:
                st.write("Day High:", data.info.get('dayHigh', 'N/A'))
                st.write("Regular Market Previous Close:", data.info.get('regularMarketPreviousClose', 'N/A'))
                st.write("Regular Market Open:", data.info.get('regularMarketOpen', 'N/A'))
                st.write("Dividend Rate:", data.info.get('dividendRate', 'N/A'))
                st.write("Dividend Yield:", data.info.get('dividendYield', 'N/A'))
                st.write("5 Yr Avg Dividend Yield:", data.info.get('fiveYearAvgDividendYield', 'N/A'))
                st.write("Beta:", data.info.get('beta', 'N/A'))
                st.write("Trailing PE:", data.info.get('trailingPE', 'N/A'))

            with col3:
                st.write("Volume:", data.info.get('volume', 'N/A'))
                st.write("Average Volume:", data.info.get('averageVolume', 'N/A'))
                st.write("Market Cap:", data.info.get('marketCap', 'N/A'))
                st.write("52 Week Low:", data.info.get('fiftyTwoWeekLow', 'N/A'))
                st.write("52 Week High:", data.info.get('fiftyTwoWeekHigh', 'N/A'))
                st.write("Currency:", data.info.get('currency', 'N/A'))
                st.write("Tradeable:", data.info.get('tradeable', 'N/A'))

            with col4:
                st.write("Profit Margins:", data.info.get('profitMargins', 'N/A'))
                st.write("Float Shares:", data.info.get('floatShares', 'N/A'))
                st.write("Quote Type:", data.info.get('quoteType', 'N/A'))
                st.write("Current Price:", data.info.get('currentPrice', 'N/A'))
                st.write("Total Cash Per Share:", data.info.get('totalCashPerShare', 'N/A'))
                st.write("Total Debt:", data.info.get('totalDebt', 'N/A'))
                st.write("Revenue Per Share:", data.info.get('revenuePerShare', 'N/A'))
    