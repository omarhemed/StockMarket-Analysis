# Stock Market Trend Analysis 

This project was created by Omar Hemed and it analyzes historical stock data for selected companies (AAPL, GOOGL, MSFT, and AMZN), providing a clear statistical summary of each stock's performance over a year. This project was built from scratch to demonstrate my ability to handle real-world financial data, create meaningful insights, and visually communicate trends in stock prices.


## Author
- Omar Hemed
- GitHub: omarhemed
- Contact: omarhemed1@hotmail.com

## Output Description
1. Once you run the code, it will fetch historical stock data for each of the chosen stocks, displaying information as follows:

Daily Stock Data Table: This includes columns such as:

- Adj Close: The closing price adjusted for stock splits and dividends.
- Close: The raw closing price of the stock.
- High: The highest price of the stock during the trading day.
- Low: The lowest price during the trading day.
- Open: The price at which the stock opened that day.
- Volume: The number of shares traded.

Each row corresponds to one trading day, capturing key data that financial analysts commonly use to observe daily trends.

## Statistical Summary for Each Stock: For each stock (AAPL, GOOGL, MSFT, AMZN), the code provides basic statistical metrics:

- Count: Total number of data points (trading days).
- Mean: Average values for the adjusted close, close, high, low, open prices, and volume, giving an idea of typical values over the year.
- Standard Deviation (std): Indicates the volatility of each stock's price. Higher values signify greater fluctuation.
- Min and Max: Lowest and highest recorded values, helping in understanding the range of each stock's price over the year.
- 25%, 50%, and 75% (quartiles): Values at different percentiles, which are helpful for assessing the distribution and central tendency.


This data provides an in-depth look at the stocks' historical performances, allowing trends and patterns to be identified at a glance.

## How to Run This Code
Follow these steps to set up and run the project on your system:

Open a Terminal (Git Bash, Command Prompt, or any terminal of your choice) and navigate to your Desktop:
```
cd Desktop
```
Clone the Repository by running:
```
git clone https://github.com/omarhemed/StockMarket-Analysis.git
```
After you succesfully clone the file into your dekstop open it in vscode or your favorite editor and type the folloiwng: 

```
cd venv
```
```
python stock_analysis.py
```
View the Results – The script will output statistical summaries and display visualizations of stock data for multiple companies.

Enjoy analyzing stock trends and exploring the charts!


Examples Results: 



![Figure_2](https://github.com/user-attachments/assets/b7c03a4e-ae0a-4e24-ade8-bb749f4a3b7a)
![Figure_3](https://github.com/user-attachments/assets/686fb680-a5e3-4166-99cf-6fcef46cc69f)
![Figure_4](https://github.com/user-attachments/assets/568addb1-7e8b-4694-935d-b122273a14dd)









