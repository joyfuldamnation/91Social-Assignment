# Write a Python program to convert the Python dictionary object (sort by key) to
# JSON data. Print the object members with indent level 4.
import json
str = {'4': 1, '6': 90, '1': 22, '2': 45, '0':23, '-1':2}
print("JSON data:")
data = json.dumps(str, sort_keys=True, indent=4)
print(data)