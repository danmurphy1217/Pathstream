import pandas as pd

pollution_df = pd.read_csv("pollution_la_2012_2016.csv")
pollution_df.head(5)

pollution_df.site_number.value_counts()

pollution_df[pollution_df["site_number"] == "11A3"]

pollution_df.loc[208, "site_number"] = 1103

pollution_df["site_number"].value_counts()

pollution_df["site_number"] = pollution_df["site_number"].astype(int)

pollution_df["site_number"].value_counts()
