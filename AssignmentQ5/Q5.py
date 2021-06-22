#Write a Python program that takes a text file as input and returns the number of words of a given text file.
def count_words(file):
    with open(file) as f:
       data = f.read()
       data.replace(",", " ")
       count = len(data.split(" "))
    return count
print(count_words("testfile.txt"))