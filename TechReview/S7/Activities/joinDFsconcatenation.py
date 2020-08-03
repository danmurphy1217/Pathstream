import pandas as pd

pollution_df_la12 = pd.read_csv("pollution_la_2012.csv")
pollution_df_la13 = pd.read_csv("pollution_la_2013.csv")

pollution_df_la12.head(5)
pollution_df_la13.head(5)

pollution_df_la1213 = pd.concat([pollution_df_la12, pollution_df_la13], ignore_index=True)

pollution_la1415 = pd.read_csv("pollution_la_2014_2015.csv")

df = pd.concat([pollution_la1415, pollution_df_la1213], ignore_index=True)

df.info()

