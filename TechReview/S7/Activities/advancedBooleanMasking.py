import pandas as pd

pollution_df = pd.read_csv("pollution_ca_2012_2016.csv")
pollution_df.head(15)

pollution_df["SO2 Mean"] < 0.05

pollution_df["CO Mean"] < 0.01

pollution_df.loc[(pollution_df["SO2 Mean"] < 0.05) & (pollution_df["CO Mean"] < 0.01)]

pollution_df.loc[(pollution_df["NO2 Mean"] > 50) & (pollution_df["City"].isin(["Burbank", "Rubidoux"]))]

pollution_df.loc[(pollution_df["City"] == "San Bernardino") & ((pollution_df["NO2 Mean"] > 10) | (pollution_df["SO2 Mean"] > 2))]
