# EX2
#   1) Create a module called utils.py and put the following functions inside:
import os


#       A) first function takes a path to a folder and writes all filenames in the folder to a specified output file
def files_in_folder(output_file, path):
    files = os.listdir(path)
    with open(output_file, "w") as file_object:
        for file in files:
            file_object.write("%s\n" % file)


#       B) second takes a path to a folder and write all filenames recursively (files of all sub folders to)
def files_in_folder_recursive(output_file, path):
    directory = os.walk(path)
    with open(output_file, "w") as file_object:
        for root, dirs, files in directory:
            for name in files:
                print(os.path.join(root, name))
                file_object.write("%s\n" % os.path.join(root, name))
    #     for files in directory:
    #         for file in files:
    #             print(file)
    #             file_object.write("%s\n" % file)


#       C) third takes a list of filenames and print the first line of each
def print_first_of_file_names(fileNameList):
    for fileName in fileNameList:
        with open(fileName) as file:
            print(file.readline())


#       D) fourth takes a list of filenames and print each line that contains an email (just look for @)
def print_all_emails(fileNameList):
    for fileName in fileNameList:
        with open(fileName) as file:
            for line in file.readlines():
                if "@" in line:
                    print(line)


#       E) fifth takes a list of md files and writes all headlines (lines starting with #) to a file Make sure your
#       module can be called both from cli and imported to another module Create a new module that imports utils.py and test each function.
def write_all_headers_to_file(output_file, fileNameList):
    mdList = []
    for fileName in fileNameList:
        with open(fileName) as file:
            for line in file.readlines():
                if "#" in line:
                    mdList.append(line)
    with open(output_file, "w") as file_object:
        for headerLine in mdList:
            file_object.write("%s\n" % headerLine)
