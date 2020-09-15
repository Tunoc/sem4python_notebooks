import csv
import matplotlib.pyplot as plt
from my_modules.Courses import Course
from my_modules.Student import Student
from my_modules.Data_sheet import DataSheet
"""Week3 - Exercise 1.8"""
#     8) Read student data into a list of Students from a csv file:
#         A) loop through the list and print each student with name, img_url and avg_grade.
#         B) sort the list by avg_grade
#         C) create a bar chart with student_name on x and avg_grade on y-axis
#     9) Make a method on Student class that can show progression of the study in % (add up ECTS from all passed courses divided by total of 150 total points (equivalent to 5 semesters))
#     10) Show a bar chart of distribution of study progression on x-axis and number of students in each category on y-axis. (e.g. make 10 categories from 0-100%)
#     Extra: Make the Datasheet class iterable so that next(data_sheet) will return the next course in the list


def readStudentDataFromCSV(input_file):
    studentList = []
    with open(input_file, "r") as file_object:
        reader = csv.reader(file_object)
        next(reader)  # next for skipping the headder of the csv file.
        prevStudent = Student("", "", None, "")  # empty instantiation
        for line in reader:
            name, gender, course, teacher, ects, classroom, grade, img_url = line
            currStudent = Student(name, gender, DataSheet(
                [Course(course, classroom, teacher, ects, grade)]), img_url)
            if prevStudent.name == currStudent.name:
                prevStudent.data_sheet.courses.append(
                    currStudent.data_sheet.courses[0])
            else:
                studentList.append(currStudent)
                prevStudent = currStudent
    return studentList


# A) loop through the list and print each student with name, img_url and avg_grade.
# B) sort the list by avg_grade
# C) create a bar chart with student_name on x and avg_grade on y-axis
def print8A(studentList):
    sortedList = []
    print("A) loop through the list and print each student with name, img_url and avg_grade.")
    for student in studentList:
        sortedList.append([student.name,
                           student.image_url, student.get_avg_grade()])
        for item in sortedList:
            print(item)


def print8B(studentList):
    sortedList = []
    print("B) sort the list by avg_grade")
    for student in studentList:
        sortedList.append([student.name,
                           student.image_url, student.get_avg_grade()])
    sortedList.sort(key=lambda x: x[2], reverse=True)
    for item in sortedList:
        print(item)


def print8C(studentList):
    sortedList = []
    print("\n" + "C) create a bar chart with student_name on x and avg_grade on y-axis")
    for student in studentList:
        sortedList.append([student.name,
                           student.image_url, student.get_avg_grade()])
    name = []
    grade = []
    sortedList.sort(key=lambda x: x[2], reverse=True)
    for item in sortedList:
        name.append(item[0])
        grade.append(item[2])
    plt.figure()
    plt.bar(name, grade)
    plt.title("Bar chart", fontsize=24)
    plt.xlabel("Names", fontsize=14)
    plt.xticks(rotation=90)
    plt.ylabel("Avg grade", fontsize=14)
    plt.show(block=True)


if __name__ == "__main__":
    studentsFromCSV = readStudentDataFromCSV("../my_resources/students.csv")
    print8A(studentsFromCSV)
    print8B(studentsFromCSV)
    print8C(studentsFromCSV)
