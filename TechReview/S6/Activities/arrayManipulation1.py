
# Two-dimensional array
arr_1 = np.array([[54, 65, 93, 90], [25, 38, 50, 32], [45, 21, 67, 87], [45, 34, 54, 84], [27, 34, 78, 95], [42, 11, 10, 52]])
arr_1.shape # num rows and cols

# sort by rows
np.sort(arr_1 , axis = 1)

# sort by cols
np.sort(arr_1 , axis = 0)


# sort by rows and cols
arr_sorted_rows = np.sort(arr_1 , axis = 1)
np.sort(arr_sorted_rows, axis=0)