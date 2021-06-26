import pandas as pd


pollution_df = pd.read_csv("pollution_la_2012_2016.csv")


pollution_df.head()

pollution_df.info()

pollution_df["date_local"] = pd.to_datetime(pollution_df["date_local"])

pollution_df["date_local"]

pollution_df["site_number"] = pollution_df["site_number"].astype(int)

pollution_df["site_number"].value_counts()
