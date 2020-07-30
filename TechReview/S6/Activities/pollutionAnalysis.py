import pandas as pd

df = pd.read_csv("pollution_ca_2012_2016.csv")

df.head(5) # or .head()

df.tail(5) # or .tail()

df.shape

df.info()


# PART TWO WITH .DESCRIBE


df.describe()

df['city'].value_counts()

df['Site Num'].value_counts()

