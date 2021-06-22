# Write a Python program to read a file line by line and store it into a list.
def filetolist(filename):
    with open(filename) as f:
        linelist= f.readlines()
        linelist = [x.strip() for x in linelist]
    return linelist
print(filetolist("testfile.txt"))