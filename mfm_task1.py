import pandas as pd
import matplotlib.pyplot as plt

#reading the bond yield from each country from seperate csv files
germany_data = pd.read_csv('data/germany_bond_yield.csv', parse_dates=['DATE'])
italy_data = pd.read_csv('data/italy_bond_yield.csv', parse_dates=['DATE'])
spain_data = pd.read_csv('data/spain_bond_yield.csv', parse_dates=['DATE'])

#now we merge the data into one DataFram using the 'DATE' column as the key
data = germany_data.merge(italy_data, on='DATE', suffixes=('_Germany', '_Italy'))
data = data.merge(spain_data, on='DATE', suffixes=('', '_Spain'))

# Set the 'DATE' column as the index
data.set_index('DATE', inplace=True)

# Calculate the risk spreads
data['Risk Spread Italy'] = data['Italy'] - data['Germany']
data['Risk Spread Spain'] = data['Spain'] - data['Germany']

# Plot the risk spreads
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Risk Spread Italy'], label='Italy')
plt.plot(data.index, data['Risk Spread Spain'], label='Spain')
plt.axhline(0, color='black', linestyle='--', alpha=0.7)  #this add a horizontal line at y=0
plt.xlabel('Date')
plt.ylabel('Risk Spread (%)')
plt.title('Risk Spreads for Italy and Spain')
plt.legend()
plt.grid(True)
plt.show()
