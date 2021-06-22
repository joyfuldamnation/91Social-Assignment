#Write a script which can read the files line by line with .log ext and print it into a
#file , while printing the data from the suffix with present date and time of the system.
from datetime import datetime

def read_and_from_input_file_and_write_in_output_file(input_files):

    out_file_obj = open('out.txt', 'w')

    for inp_file in input_files:
        if not inp_file.endswith('.log'):
            continue

        inp_file_obj = open(inp_file)
        for line in inp_file_obj.readlines():
            curr_date_time_obj = datetime.now()
            curr_date_time_str = curr_date_time_obj.strftime("%d/%m/%Y %H:%M:%S")
            out_file_obj.write(curr_date_time_str + ' ' + line)

        inp_file_obj.close()

        print(
            "Successfully written log of file " + inp_file +
            ' in output file i.e out.txt ' + "\n"
        )

    out_file_obj.close()


if __name__ == "__main__":
    print("Enter the length of array \n")
    LENGTH_OF_ARRAY = int(input())
    INPUT_ARRAY = []

    while len(INPUT_ARRAY) < LENGTH_OF_ARRAY:
        print("Enter the Filename : \n")
        INPUT_ARRAY.append(input())

    read_and_from_input_file_and_write_in_output_file(INPUT_ARRAY)