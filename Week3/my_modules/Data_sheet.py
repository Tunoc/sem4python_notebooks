"""Week3 - Exercise 1.1 - 1.6"""
#     1) Create 3 classes: Student, DataSheet and Course
#     2) A student has a data_sheet and a data_sheet has multiple courses in particular order
#     3) Each course has name, classroom, teacher, ETCS and optional grade if course is taken.
#     4) In Student create init() so that a Student can be initiated with name, gender, data_sheet and image_url
#     5) In DataSheet create a method to get_grades_as_list()
#     6) In student create a method: get_avg_grade()


class DataSheet:
    """A simple datasheet that contains multiple courses in particular order"""

    def __init__(self, courses):
        self.courses = courses

    def __repr__(self):
        return 'Datasheet(%r)' % (self.courses)

    def __str__(self):
        return 'List of courses: {courses}.'.format(
            courses=self.courses)

    def get_grades_as_list(self):
        """Gets a list of all grades, connected to a student"""
        grades = []
        for course in self.courses:
            grades.append(int(course.grade))
        return grades
