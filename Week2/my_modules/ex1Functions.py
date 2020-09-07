import argparse
import csv
import platform

if platform.system() == 'Windows':
    newline = ''
else:
    newline = None


# def print_file_content(file) that can print content of a csv file to the console
def print_file_content(file):
    with open(file) as file_object:
        reader = csv.reader(file_object)
        for row in reader:
            print("Row #" + str(reader.line_num) + " " + str(row))


# def write_list_to_file(output_file, lst) that can take a list of tuple and write each element to a new line in file
# rewrite the function so that it gets an arbitrary number of strings instead of a list
def write_list_to_file(output_file, lst):
    with open(output_file, 'a') as file_object:
        for line in lst:
            file_object.write('%s\n' % line)


# 1c) def read_csv(input_file) that take a csv file and read each row into a list
def read_csv(input_file):
    returnList = []
    with open(input_file, "r") as file_object:
        returnList = file_object.read().splitlines()
        # for line in file_object:
        #    returnList.append(line)

        #reader = csv.reader(file_object)
        # for row in reader:
        #    returnList.append(row)
    return returnList


# 2) Add a functionality so that the file can be called from cli with 2 arguments
#        A) path to csv file
#        B) an argument --file file_name that if given will write the content to file_name or otherwise will print it to the console.
if(__name__ == '__main__'):
    parser = argparse.ArgumentParser(
        description="A program to read from a specific file, and write to a specific file or write it to the console.")
    parser.add_argument('Input_File', help='Name of the file to read from.')
    parser.add_argument('--file', help='Name of the file to write to.')
    args = parser.parse_args()

    if args.file is None:
        print_file_content(args.Input_File)
    else:
        lines = read_csv(args.Input_File)
        write_list_to_file(args.file, lines)
        print(lines)
