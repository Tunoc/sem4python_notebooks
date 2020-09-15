import statistics as stats
"""Week3 - Exercise 1.1 - 1.6 + 1.9"""
#     1) Create 3 classes: Student, DataSheet and Course
#     2) A student has a data_sheet and a data_sheet has multiple courses in particular order
#     3) Each course has name, classroom, teacher, ETCS and optional grade if course is taken.
#     4) In Student create init() so that a Student can be initiated with name, gender, data_sheet and image_url
#     5) In DataSheet create a method to get_grades_as_list()
#     6) In student create a method: get_avg_grade()
#     9) Make a method on Student class that can show progression of the study in % (add up ECTS from all passed courses divided by total of 150 total points (equivalent to 5 semesters))


class Student:
    """A simple student class, consisting of a name, gender, age and data_sheet"""

    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def __repr__(self):
        return 'Student(%r, %r, %r, %r)' % (self.name, self.gender, self.data_sheet, self.image_url)

    def __str__(self):
        return '{name} is a {gender} student. The student has this imgUrl {img_url} and this data_sheet {datasheet}.'.format(
            name=self.name, gender=self.gender, img_url=self.image_url, datasheet=self.data_sheet)

    def get_avg_grade(self):
        """Gets a avg of all grades, connected to a student
        https://docs.python.org/3/library/statistics.html#statistics.mean"""
        avgSumOfGrades = stats.mean(self.data_sheet.get_grades_as_list())
        return avgSumOfGrades

    def get_progression(self):
        """
        Make a method on Student class that can show progression of the study in % 
        (add up ECTS from all passed courses divided by total of 150 total points (equivalent to 5 semesters))
        """
        totalECTS = 0
        for course in self.data_sheet.courses:
            if int(course.grade) > 0:
                totalECTS += int(course.ECTS)
        return((totalECTS/150)*100)
