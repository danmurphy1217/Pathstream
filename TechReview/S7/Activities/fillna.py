pollution_df = pd.read_csv("pollution_la_2012_2016.csv")
pollution_df.head()

pollution_df.info()

pollution_df["co_units"].value_counts(dropna=False)

pollution_df["co_units"].fillna("Parts per million", inplace=True)
pollution_df["co_units"].value_counts(dropna=False)

pollution_df["no2_units"].value_counts(dropna=False)

pollution_df["no2_units"].fillna("Parts per billion", inplace=True)
pollution_df["no2_units"].value_counts(dropna=False)

pollution_df["no2_mean"].mean()


pollution_df["o3_mean"].mean()

pollution_df["o3_mean"].fillna(pollution_df["o3_mean"].mean(), inplace=True)
pollution_df.head()