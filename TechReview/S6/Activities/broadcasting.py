import numpy as np

home_price = [510000, 459000, 385000, 499000, 474000, 376000, 453000, 394000]
square_footage = [2100, 1950, 1586, 2240, 1700, 1320, 1670, 1430]

home_price_array = np.array(home_price)
square_footage_array = np.array(square_footage)

tax = home_price_array*.01
tax

home_price_array/square_footage_array

tax/square_footage_array