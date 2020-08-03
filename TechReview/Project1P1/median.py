length = len(data)
sortedData = sorted(data)

if length % 2 == 0: 
  median = (sortedData[length//2] + sortedData[length//2 - 1])/2
else:
  median = sortedData[length//2]

 
print(f"The median of your data is {median}")
