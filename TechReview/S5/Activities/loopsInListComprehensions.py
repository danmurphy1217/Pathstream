# terminal activity
[[col for col in range(1, 4)] for row in range(3)]

population_by_country = [
    ["Year", 2017, 2018, 2019],
    ["Canada", 36.54, 37.06, 37.59],
    ["US", 325.1, 327.2, 328.2],
    ["UK", 65.82, 66.27, 66.65]
]
matrix_length = len(population_by_country)

transposed_population = [[row[i] for row in population_by_country] for i in range(matrix_length)] # write your nested list comprehension here
print(transposed_population)



# box measurements in inches: length, depth, height
box_measurements_in = [[18, 18, 16],
                       [18, 18, 24],
                       [16, 12, 12],
                       [24, 20, 46]]

box_measurements_cm = [[item * 2.54 for item in sublist] for sublist in box_measurements_in]

print(box_measurements_cm)