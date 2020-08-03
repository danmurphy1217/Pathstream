import pandas as pd

pollution_df_la1216 = pd.read_csv("pollution_la_2012_2016.csv")
la_co_df = pd.read_csv("la_co_measurements.csv")


pollution_df_la1216.info()
la_co_df.info()

pollution_df_la1216.head(5)

pollution_df_la_joined = pollution_df_la1216.merge(la_co_df)
pollution_df_la_joined.info()

la_so2_df = pd.read_csv("la_so2_measurements.csv")
la_so2_df.head()

pollution_df_la_joined = pollution_df_la_joined.merge(la_so2_df)
pollution_df_la_joined.info()

site_addresses_df = pd.read_csv("site_addresses.csv")
site_addresses_df.info()

pollution_df_la_joined.merge(site_addresses_df)
pollution_df_la_joined.head()


pollution_df_la_joined.info()


