# Insert code here
import numpy as np
import pandas as pd

lst = [44,38,72,89,343,534,123,75,98,65]

# Convert the list above into a Series and save the Series as a variable
my_first_series = pd.Series(lst)
# Now view the series
my_first_series

hp_characters = ["Potter", "Weasley", "Granger", "Snape", "Dumbledore"]

lst_to_series = pd.Series(hp_characters)
lst_to_series

pd.Series(data = hp_characters, index = ["Harry", "Ron", "Hermoine", "Severus", "Albus"])

dictionary = {"Freddrick": 27, "Penny": 24, "Katie": 23, "Kevin": 25}

pd.Series(dictionary)

array = np.array([34, 35, 66, 84, 35, 65, 34, 21, 37, 32, 95])
pd.Series(array)