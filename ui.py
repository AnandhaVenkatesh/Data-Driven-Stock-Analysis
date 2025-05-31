import streamlit as st
import mysql.connector
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# Database connection
engine = create_engine("mysql+mysqlconnector://root:Venkat123@localhost/StockAnalysis")

col = st.sidebar.selectbox("Select the page",['Home Page','Volatility Analysis','Cumulative Return Over Time','Sector wise Performance',
                                              'Stock Price Correlation','Top Gainers and Loosers'])

if col == "Home Page":
    st.markdown("<h1 style='color:red;'> Data-Driven Stock Analysis</h1>",unsafe_allow_html=True)
    st.image("E:\StockAnalysis\download(1).jpg",use_container_width=True)

elif col == "Volatility Analysis":
    st.subheader("📊 Top 10 Most Volatile Stocks")
    df = pd.read_sql("SELECT * FROM stockanalysis.top_10_most_volatile_stocks;",engine)
    df.index = df.index + 1
    st.dataframe(df)

    st.markdown("### 🔍 Volatility Bar Chart")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df.reset_index(drop=True), x='Ticker', y='Volatility', palette='viridis', ax=ax)
    ax.set_title("Top 10 Most Volatile Stocks (Standard Deviation of Daily Returns)", fontsize=14)
    ax.set_xlabel("Ticker")
    ax.set_ylabel("Volatility")
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

elif col == "Cumulative Return Over Time":
    st.subheader("📊 Cumulative Return Top 5")
    df1 = pd.read_sql("SELECT * FROM stockanalysis.cumulative_return_top_5;",engine)
    df1.index = df1.index + 1
    st.dataframe(df1)

    st.markdown("### 📈 Cumulative Return Line Chart")

    st.image(r"E:\StockAnalysis\Project\analysis_results_new\Cumulative_Return_Top_5_LineChart.png", use_container_width=True)
    # fig, ax = plt.subplots(figsize=(24, 12))
    # sns.lineplot(data=df1.reset_index(drop=True), x='date', y='CumulativeReturn', hue='Ticker', marker='o', ax=ax)
    # ax.set_title("📈 Cumulative Return Over Time (Top 5 Stocks)")
    # ax.set_xlabel("Date")
    # ax.set_ylabel("Cumulative Return")
    # ax.legend(title="Ticker")
    # ax.grid(True)
    # plt.xticks(rotation=45)
    # st.pyplot(fig)

elif col == "Sector wise Performance":
    st.subheader("📊 Sector Wise Performance")
    df2 = pd.read_sql("SELECT * FROM stockanalysis.sector_performance;", engine)
    df2.index = df2.index + 1
    st.dataframe(df2)

    df2_sorted = df2.sort_values(by='YearlyReturn', ascending=True)

    st.markdown("### 📊 Average Yearly Return by Sector")

    st.image(r"E:\StockAnalysis\Project\analysis_results_new\sector_performance_chart.png", use_container_width=True)
    

elif col == "Stock Price Correlation":
    st.subheader("📊 Stock Price Correlation")
    df3 = pd.read_sql("SELECT * FROM stockanalysis.sector_performance;", engine)
    df3.index = df3.index + 1
    st.dataframe(df3)

    st.subheader("📉 Sector-wise Performance (Bar Chart)")

    st.image("E:/StockAnalysis/Project/analysis_results_new/Stock_Correlation_Heatmap.png", use_container_width=True)


elif col == "Top Gainers and Loosers":
    st.subheader("📊 Monthly Top Gainers and Losers")
    df5 = pd.read_sql("SELECT * FROM monthly_top_gainers_losers", engine)
    df5.index = df5.index + 1
    st.dataframe(df5)

    st.subheader("📉 Top 5 Gainers and Losers by Month")
    st.image(r"E:\StockAnalysis\Project\analysis_results_new\Top_5_Gainers_Losers_2023-10.png", use_container_width=True)
    st.image(r"E:\StockAnalysis\Project\analysis_results_new\Top_5_Gainers_Losers_2023-11.png", use_container_width=True)
    st.image(r"E:\StockAnalysis\Project\analysis_results_new\Top_5_Gainers_Losers_2023-12.png", use_container_width=True)
    st.image(r"E:\StockAnalysis\Project\analysis_results_new\Top_5_Gainers_Losers_2024-01.png", use_container_width=True)
    st.image(r"E:\StockAnalysis\Project\analysis_results_new\Top_5_Gainers_Losers_2024-02.png", use_container_width=True)
    st.image(r"E:\StockAnalysis\Project\analysis_results_new\Top_5_Gainers_Losers_2024-03.png", use_container_width=True)
    st.image(r"E:\StockAnalysis\Project\analysis_results_new\Top_5_Gainers_Losers_2024-04.png", use_container_width=True)
    st.image(r"E:\StockAnalysis\Project\analysis_results_new\Top_5_Gainers_Losers_2024-05.png", use_container_width=True)
    st.image(r"E:\StockAnalysis\Project\analysis_results_new\Top_5_Gainers_Losers_2024-06.png", use_container_width=True)
    st.image(r"E:\StockAnalysis\Project\analysis_results_new\Top_5_Gainers_Losers_2024-07.png", use_container_width=True)
    st.image(r"E:\StockAnalysis\Project\analysis_results_new\Top_5_Gainers_Losers_2024-08.png", use_container_width=True)
    st.image(r"E:\StockAnalysis\Project\analysis_results_new\Top_5_Gainers_Losers_2024-09.png", use_container_width=True)
    st.image(r"E:\StockAnalysis\Project\analysis_results_new\Top_5_Gainers_Losers_2024-10.png", use_container_width=True)
    st.image(r"E:\StockAnalysis\Project\analysis_results_new\Top_5_Gainers_Losers_2024-11.png", use_container_width=True)


