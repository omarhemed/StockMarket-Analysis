# Necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import yfinance as yf

# Set up Seaborn style for better looking plots
sns.set_style('whitegrid')

tech_stocks = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']

# Define the date range for the stock data
end_date = datetime.now()
start_date = datetime(end_date.year - 1, end_date.month, end_date.day)

# Fetch stock data for each stock in tech_stocks and store them in individual DataFrames
stock_data = {}  
for stock in tech_stocks:
    print(f"Fetching data for {stock}...")
    stock_data[stock] = yf.download(stock, start=start_date, end=end_date)

# Function to display basic statistics for each stock
for stock in tech_stocks:
    print(f"\nBasic Statistics for {stock}:")
    print(stock_data[stock].describe())

# Plot adjusted closing prices for each stock
plt.figure(figsize=(14, 7))
for stock in tech_stocks:
    stock_data[stock]['Adj Close'].plot(label=stock)
plt.title('Adjusted Closing Price of Tech Stocks')
plt.xlabel('Date')
plt.ylabel('Adjusted Closing Price (USD)')
plt.legend()
plt.show()

# Plot the trading volume for each stock
plt.figure(figsize=(14, 7))
for stock in tech_stocks:
    stock_data[stock]['Volume'].plot(label=stock)
plt.title('Daily Trading Volume of Tech Stocks')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.show()

# Calculate moving averages (10, 20, and 50 days) for each stock
moving_averages = [10, 20, 50]
for stock in tech_stocks:
    for ma in moving_averages:
        column_name = f"MA for {ma} days"
        stock_data[stock][column_name] = stock_data[stock]['Adj Close'].rolling(ma).mean()

# Plot the adjusted close price with moving averages for Apple stock 
plt.figure(figsize=(14, 7))
stock_data['AAPL'][['Adj Close', 'MA for 10 days', 'MA for 20 days', 'MA for 50 days']].plot()
plt.title('Apple Stock - Adjusted Close Price and Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.show()

# Calculate daily returns for each stock
for stock in tech_stocks:
    stock_data[stock]['Daily Return'] = stock_data[stock]['Adj Close'].pct_change()

# Plot the daily returns for Apple stock
plt.figure(figsize=(14, 7))
stock_data['AAPL']['Daily Return'].plot(legend=True, linestyle='--', marker='o')
plt.title('Apple Stock - Daily Returns')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.show()

# Plot histogram of daily returns for Apple stock to understand return distribution
plt.figure(figsize=(12, 6))
sns.histplot(stock_data['AAPL']['Daily Return'].dropna(), bins=100, color='purple')
plt.title('Distribution of Apple Stock Daily Returns')
plt.xlabel('Daily Return')
plt.show()

# Combine adjusted close prices of all stocks into one dataframe for correlation analysis
closing_prices = pd.DataFrame({stock: stock_data[stock]['Adj Close'] for stock in tech_stocks})

# Calculate daily return percentages for each stock and store in a dataframe
daily_returns = closing_prices.pct_change()

# Jointplot comparing Google and Microsoft daily returns
sns.jointplot(x='GOOGL', y='MSFT', data=daily_returns, kind='scatter', color='seagreen')
plt.show()

# Pairplot to visualize correlation between the daily returns of each stock
sns.pairplot(daily_returns.dropna())
plt.show()

# Plot heatmap to visualize correlation matrix for daily returns
plt.figure(figsize=(10, 8))
sns.heatmap(daily_returns.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Daily Returns')
plt.show()

# Risk-Return Analysis: Plotting Expected Returns vs. Risk (Standard Deviation)
plt.figure(figsize=(10, 7))
plt.scatter(daily_returns.mean(), daily_returns.std(), alpha=0.5, s=100)

plt.xlabel('Expected Return')
plt.ylabel('Risk (Standard Deviation)')
plt.title('Risk vs. Expected Return')

# Label each stock on the risk-return plot
for stock in daily_returns.columns:
    plt.annotate(stock, (daily_returns.mean()[stock], daily_returns.std()[stock]),
                 textcoords="offset points", xytext=(5,5), ha='center')

plt.show()

print("Analysis complete.")
