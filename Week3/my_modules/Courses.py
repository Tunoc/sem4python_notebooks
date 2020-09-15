"""Week3 - Exercise 1.1 - 1.6"""
#     1) Create 3 classes: Student, DataSheet and Course
#     2) A student has a data_sheet and a data_sheet has multiple courses in particular order
#     3) Each course has name, classroom, teacher, ETCS and optional grade if course is taken.
#     4) In Student create init() so that a Student can be initiated with name, gender, data_sheet and image_url
#     5) In DataSheet create a method to get_grades_as_list()
#     6) In student create a method: get_avg_grade()


class Course:
    """A simple course class, consisting of a name, classroom, teacher, ETCS and an optional grade if the class is taken"""

    def __init__(self, name, classroom, teacher, ECTS, grade=None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ECTS
        self.grade = grade

    def __repr__(self):
        return 'Courses(%r, %r, %r, %r, %r)' % (self.name, self.classroom, self.teacher, self.ECTS, self.grade)

    def __str__(self):
        return '{name} taught by {teacher} in {classroom}. The course {courseName} gives {ECTS} ECTS and your personal grade is {grade}.'.format(
            name=self.name, teacher=self.teacher, classroom=self.classroom, courseName=self.name, ECTS=self.ECTS, grade=self.grade)
