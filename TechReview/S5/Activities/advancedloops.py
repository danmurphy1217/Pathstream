# Transforming a for loop
customer_id = [1023.0, 1024.0, 1025.0, 1026.0, 1027.0, 1028.0, 1029.0, 1030.0, 1031.0, 1032.0, 1033.0, 1034.0, 1035.0, 1036.0, 1037.0, 1038.0, 1039.0, 1040.0, 1041.0, 1042.0, 1043.0, 1044.0, 1045.0, 1046.0, 1047.0, 1048.0, 1049.0, 1050.0, 1051.0, 1052.0, 1053.0, 1054.0, 1055.0]

# Takes in customer id's casts them to integers, returning a new list
def clean_ids(id_list):
    return [int(id) for id in id_list]

print(clean_ids(customer_id))

