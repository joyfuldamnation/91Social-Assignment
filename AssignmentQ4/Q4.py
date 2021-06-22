# Write a Python program to sort a list of dictionaries using Lambda.
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2',
# 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7,
# 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
def lambda_sort_dict(models):
    print("before sort:")
    print(models)
    models_sort = sorted(models, key = lambda x: x['color'])
    print("Sorting using lambda:")
    print(models_sort)

print(lambda_sort_dict([{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
))