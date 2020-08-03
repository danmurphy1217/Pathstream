

diff_sqaured = 0
sum_diffsquared = 0


for val in data:
  diff_squared = (val-average)**2 
  sum_diffsquared = diff_squared + sum_diffsquared
stddev = (sum_diffsquared/len(data))**0.5
