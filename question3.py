def average_closing_price(stock_data, stock_symbol, start_date, end_date):
    total_price = 0
    count = 0
    for data in stock_data:
        symbol, date, closing_price = data
        if symbol == stock_symbol and start_date <= date <= end_date:
            total_price += closing_price
            count += 1
    if count == 0:
        return None 
    else:
        return total_price / count

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    ("MSFT", "2021-01-02", 225.0),
    ("GOOGL", "2021-01-01", 1800.0),
    ("GOOGL", "2021-01-02", 1850.0),
]

avg_price = average_closing_price(stock_data, "AAPL", "2021-01-01", "2021-01-02")
print(f"Average closing price of AAPL from 2021-01-01 to 2021-01-02: {avg_price}")
