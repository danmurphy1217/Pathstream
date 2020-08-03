pollution_df = pd.read_csv("pollution_la_2012_2016.csv")

pollution_df.head()

pollution_df.rename(columns={"Site Num":"Site Number"}, inplace = True) 
pollution_df.head()

pollution_df.rename(columns={"Address": "Test Site Address"}, inplace = True) 
pollution_df.head()

pollution_df.columns = [col.replace(" ", "_").lower() for col in pollution_df.columns] 
pollution_df.head()