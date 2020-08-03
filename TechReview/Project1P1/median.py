length = len(data)
sorted_data = sorted(data)

if length % 2 == 0: 
  median = (sorted_data[length//2] + sorted_data[length//2 - 1])/2
else:
  median = sorted_data[length//2]

 
print(f"The median of your data is {median}")
