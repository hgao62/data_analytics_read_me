import pandas as pd
# Interview question 1 : calculate the net position of a stock

data = {
    'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
    'Counter party name': ['Investor A', 'Investor B', 'Investor C', 'Investor D'],
    'Ticker symbol': ['AAPL', 'GOOGL', 'MSFT', 'AAPL'],
    'Buy/Sell': ['BUY', 'SELL', 'BUY', 'SELL'],
    'Number of shares': [100, 150, 200, 50],
    'Trade price': [150.0, 2800.0, 300.0, 155.0]
}
df = pd.DataFrame(data)

# Convert 'Buy/Sell' into signed quantities: BUY = +shares, SELL = -shares
df['signed_shares'] = df.apply(
    lambda row: row['Number of shares'] if row['Buy/Sell'] == 'BUY' else -row['Number of shares'],
    axis=1
)

# Group by ticker and sum the signed shares to get net position
net_position = df.groupby('Ticker symbol')['signed_shares'].sum().reset_index()
net_position.rename(columns={'signed_shares': 'net_position'}, inplace=True)

print(net_position)
