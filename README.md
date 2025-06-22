# 📈 Stock Price Tracker (NSE) – Streamlit App

A beginner-friendly Streamlit web app that lets users explore historical stock prices and fundamental data for companies listed on the **National Stock Exchange of India (NSE)** via the `yfinance` API.

---

## 🔍 Features

- **Searchable dropdown** to select any NSE-listed stock  
- **Historical monthly closing price** chart using `streamlit`’s line chart  
- Real-time financial metrics displayed in a clean, four-column layout:
  - Symbol, Country, Sector, Previous Close, Open, Daily Low/High  
  - Volume, Market Cap, Beta, P/E, Dividend Yield, etc.  
- Custom CSS styling for a consistent look & feel  
- Balloon animation on search for UX flair

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** (UI Framework)
- **pandas** (Data manipulation)
- **yfinance** (Stock API)
- **matplotlib** (for any additional plotting)

---

🧠 How It Works
- Loads NSE-listed stock symbols from the provided CSV.
- User selects a symbol via a dropdown form.
- On submission, app fetches price data and company info using yfinance.
- Monthly closing price is visualized, along with key metrics in structured columns.

---

  👤 Author: Srijith Shaibu
Project: Stock Price Tracker – NSE
