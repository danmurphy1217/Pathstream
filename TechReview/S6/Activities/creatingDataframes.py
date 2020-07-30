import numpy as np
import pandas as pd

nested_lst = [[1,2,3],[4,5,6],[7,8,9]]
nested_lst

# Convert the nested list above into a DataFrame and save the DataFrame as a variable
my_first_df = pd.DataFrame(nested_lst)
# Now view the DataFrame
my_first_df

employees = [["Phil", 45, 100000],["Jan", 40, 110000],["Rodney", 55, 86000]]
employees

df = pd.DataFrame(employees, columns = [
    "name", "age", "salary"
])
df

dictionary = {"user": ["Bill", "Gordon", "Linda", "Marel"], 
              "email": ["bill@company.com", "gordon@company.com", "linda@company.com", "marel@company.com"], 
              "password": ["billrocks85", "itsGORDO", "password1!", "Margolos43"]}
dictionary

pd.DataFrame(dictionary)

array = np.array([[6543,35431,5745],[341,342325,45752],[4352,84369,54839],[98674,40462,8295]])
array

pd.DataFrame(array)