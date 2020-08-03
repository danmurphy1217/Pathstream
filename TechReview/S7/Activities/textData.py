import pandas as pd

pollution_df = pd.read_csv("pollution_la_2012_2016.csv")

pollution_df["test_site_address"] = pollution_df["test_site_address"].str.lower()
pollution_df["test_site_address"].unique()

pollution_df["test_site_address"] = pollution_df["test_site_address"].str.replace("7201", "7205")
pollution_df["test_site_address"].unique()

pollution_df["test_site_address"] = pollution_df["test_site_address"].str.replace("n main st", "main st n")
pollution_df["test_site_address"].unique()

