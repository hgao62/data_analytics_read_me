import pandas as pd

# ✅ Task:
# For each symbol, compute:

# Daily PnL

# Cumulative PnL

# Net cash flow = (position_today - position_prev) * price_today

# Add the following columns:

# daily_pnl

# cumulative_pnl

# net_cash_flow

# Use the following formulas for calculations:
#Daily PnL = (Today’s Price - Yesterday’s Price) * Yesterday’s Position
#Net Cash Flow = (Today’s Position - Yesterday’s Position) * Today’s Price

# Input
data = {
    'date': [
        '2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02',
        '2024-01-03', '2024-01-03', '2024-01-04', '2024-01-04'
    ],
    'symbol': ['AAPL', 'GOOG', 'AAPL', 'GOOG', 'AAPL', 'GOOG', 'AAPL', 'GOOG'],
    'price': [150, 2800, 152, 2820, 148, 2810, 149, 2835],
    'position': [10, 5, 10, 4, 5, 4, 5, 6]
}
df = pd.DataFrame(data)
df['date'] = pd.to_datetime(df['date'])

# Sort for correct groupby operations
df = df.sort_values(['symbol', 'date'])

# Shift position and price within each symbol
df['position_prev'] = df.groupby('symbol')['position'].shift(1)
df['price_prev'] = df.groupby('symbol')['price'].shift(1)

# Daily PnL = (price_t - price_t-1) * position_t-1
df['daily_pnl'] = (df['price'] - df['price_prev']) * df['position_prev']
df['daily_pnl'] = df['daily_pnl'].fillna(0)

# Cumulative PnL
df['cumulative_pnl'] = df.groupby('symbol')['daily_pnl'].cumsum()

# Net Cash Flow = (position_t - position_t-1) * price_t
df['net_cash_flow'] = (df['position'] - df['position_prev']) * df['price']
df['net_cash_flow'] = df['net_cash_flow'].fillna(0)

# Final output
df = df[['date', 'symbol', 'price', 'position', 'daily_pnl', 'cumulative_pnl', 'net_cash_flow']]
print(df)
