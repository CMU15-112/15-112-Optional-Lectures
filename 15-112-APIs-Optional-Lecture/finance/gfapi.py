from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data

#nasdaq
param = {
    'q': "BGS", # Stock symbol (ex: "AAPL")
    'i': "86400", # Interval size in seconds ("86400" = 1 day intervals)
    'x': "NASD", # Stock exchange symbol on which stock is traded (ex: "NASD")
    'p': "1Y" # Period (Ex: "1Y" = 1 year)
}

df = get_price_data(param)
print(df)


params = [
    # Dow Jones
    {
        'q': ".DJI",
        'x': "INDEXDJX",
    },
    # NYSE COMPOSITE (DJ)
    {
        'q': "NYA",
        'x': "INDEXNYSEGIS",
    },
    # S&P 500
    {
        'q': ".INX",
        'x': "INDEXSP",
    }
]
period = "1Y"

df = get_prices_data(params, period)
# print(df)
