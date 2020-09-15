import csv
import random
from my_modules.Courses import Course
from my_modules.Student import Student
from my_modules.Data_sheet import DataSheet

"""Week3 - Exercise 1.7"""
#     7) Create a function that can generate n number of students with random: name, gender, courses (from a fixed list of course names), grades, img_url
#       A) Let the function write the result to a csv file with format stud_name, course_name, teacher, ects, classroom, grade, img_url


def generate_random_students(numberOfStudentsPrGender):
    """Create a function that can generate n number of students with random:
    name, gender, courses (from a fixed list of course names), grades, img_url"""

    students = []
    student_names = readFromCSVMaleAndFemale(
        "./my_resources/FirstNamesAndGender.csv", numberOfStudentsPrGender)
    listOfCourses = generate_courses()
    for id, nameList in enumerate(student_names):
        students.append(build_students(id, nameList, listOfCourses))
    return students[0] + students[1]


def build_students(gender, nameList, listOfCourses):
    """Build students with all the generated information"""
    builtStudents = []
    pictures = ["https://tinyurl.com/yxz2o5zd",
                "https://tinyurl.com/y4cufl2s"]
    sur_names = ["Kim", "Lee", "Park", "Jung",
                 "Choi", "Cho", "Kang", "Yoon", "Lim", "Oh"]
    grades = ["-03", "00", "02", "4", "7", "10", "12"]
    for name in nameList:
        tempName = name + " " + random.choice(sur_names)
        tempGender = ("Female", "Male")[gender == 0]
        tempDataSheet = DataSheet(random.choices(
            listOfCourses, k=random.randrange(3, 4)))
        for course in tempDataSheet.courses:
            course.grade = random.choice(grades)
        tempPictures = pictures[gender]
        builtStudents.append(Student(tempName, tempGender,
                                     tempDataSheet, tempPictures))
    return builtStudents


def generate_courses():
    """Generate the courses for the randomly generated students"""

    courses = ["Machine Learning", "Security",
               "JavaScript", "Game Development", "Internet Of Things", "Python",
               "Computer graphics", "Animation", "Movie watching", "Go home club"]
    teachers = ["Jack the Ripper", "Jeffrey Dahmer", "Harold Shipman",
                "John Wayne Gacy", "H.H. Holmes", "Pedro Lopez", "Ted Bundy"]
    classroom = ["101", "102", "103", "104", "105"]
    ECTS = [5, 10, 15, 30]

    generatedCourses = []
    for course in courses:
        generatedCourses.append(Course(course, random.choice(
            classroom), random.choice(teachers), random.choice(ECTS)))
    return generatedCourses


def readFromCSVMaleAndFemale(CSVfile, amount):
    """A simple function that reads a CSV file, and returns a list of names based on gender and amount"""

    males = []
    females = []
    with open(CSVfile) as file_object:
        reader = csv.reader(file_object)
        # next for skipping the headder of the csv file.
        next(reader)
        for line in reader:
            # line[1] = gender "B" or "G".. line[0] = firstName
            if line[1] == "B":
                males.append(line[0])
            else:
                females.append(line[0])
    #k = amount
    return [random.choices(males, k=amount), random.choices(females, k=amount)]


# 7A) Let the function write the result to a csv file with format stud_name, course_name, teacher, ects, classroom, grade, img_url
def writeToCSVfile(output_file, listOfCompleteStudents):
    """The function that writes all the students to a CSV file with the firmat;
    stud_name, course_name, teacher, ects, classroom, grade, img_url"""
    with open(output_file, "w") as file_object:
        output_writer = csv.writer(file_object)
        output_writer.writerow(["Student_name", "Gender", "Course_name",
                                "Teacher", "ECTS", "Classroom", "Grade", "Img_url"])
        for student in listOfCompleteStudents:
            for course in student.data_sheet.courses:
                output_writer.writerow([student.name, student.gender, course.name, course.teacher,
                                        course.ECTS, course.classroom, course.grade, student.image_url])
        # for student in listOfCompleteStudents:
        #    file_object.write("%s\n" % student)


if __name__ == "__main__":
    students = generate_random_students(5)
    writeToCSVfile("../my_resources/students.csv", students)
