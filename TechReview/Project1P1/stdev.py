# code from mean.py
sumData = 0
for i in data:
  sumData = sumData + i
average = sumData/len(data)


diffSqaured = 0
sumDiffSquared = 0


for val in data:
  diffSqaured = (val-average)**2 
  sumDiffSquared = diffSqaured + sumDiffSquared
stddev = (sumDiffSquared/len(data))**0.5
