import pandas as pd

volunteer_df = pd.read_csv("volunteers.csv")
volunteer_df

volunteer_df[volunteer_df.occupation.str.contains("driver")]

volunteer_df[(volunteer_df.occupation.str.contains("driver")) | (volunteer_df.occupation.str.contains("student"))]

volunteer_df[volunteer_df.city.str.startswith("San")]