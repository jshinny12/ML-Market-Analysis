# compontn for data analysis

# Import necessary packages
import pandas as pd
import numpy as np

!kaggle datasets download -d 'stock-data-for-ml-competition'
!unzip stock-data-for-ml-competition.zip
df = pd.read_csv('stock_data.csv')

df.dropna(inplace=True)
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df.set_index('date', inplace=True)
df.sort_index(inplace=True)

df['returns'] = np.log(df['close']) - np.log(df['close'].shift(1))
df['direction'] = np.where(df['returns'] > 0, 1, -1)
df['volatility'] = df['returns'].rolling(window=252).std() * np.sqrt(252)

train_data = df.loc[df.index.year < 2020]
test_data = df.loc[df.index.year == 2020]
