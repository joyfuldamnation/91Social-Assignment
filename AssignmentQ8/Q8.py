# Program to Generate random logs and write in a file , once the file size reaches 2Mb
# open new file and continue writing
from pathlib import Path
def generate_random_logs_file():
    counter = 1
    while True:
        filename = str(counter) + '_log.txt'
        print('File : ' + filename + ' created')
        file_obj = open(filename, 'a')
        while Path(filename).stat().st_size <= 2 * 1000000:
            file_obj.write('random')
        file_obj.close()
        counter += 1
        print('File : '+ filename + ' reached 2MB')
if __name__ == "__main__":
    generate_random_logs_file()