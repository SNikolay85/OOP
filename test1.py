class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __average_grades(self):
         sum_ = 0
         num_course = []
         for course, grade in self.grades.items():
            num_course += grade
            length = len(num_course)
            for number in grade:
                sum_ += number
         average = sum_/length
         return round(average, 2)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Mentor!')
            return
        if self.__average_grades() > other.__average_grades():
            print(f'Средний балл выше имеет студент {self.name} \n')
        else:
            print(f'Средний балл выше имеет студент {other.name} \n')

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def grades_lecture(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in self.courses_in_progress and course in lecture.courses_attached:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return print('Ошибка')
    def __str__(self):

        message = (f'Студент: \n'
                   f'Имя: {self.name} \n'
                   f'Фамилия: {self.surname} \n'
                   f'Средняя оценка за домашние задания: {self.__average_grades()} \n'
                   f'Курсы в процессе изучения: {self.courses_in_progress} \n'
                   f'Завершенные курсы: {self.finished_courses} \n')
        return message

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __average_grades(self):
         sum_ = 0
         num_course = []
         for course, grade in self.grades.items():
            num_course += grade
            length = len(num_course)
            for number in grade:
                sum_ += number
         average = sum_/length
         return round(average, 2)

    def __lt__(self, other):
        if not isinstance(other, Mentor):
            print('Not a Mentor!')
            return
        if self.__average_grades() > other.__average_grades():
             print(f'Средний балл выше имеет лектор {self.name} \n')
        else:
            print(f'Средний балл выше имеет лектор {other.name} \n')

    def __str__(self):
        message = (f'Лектор: \n'
                   f'Имя: {self.name} \n'
                   f'Фамилия: {self.surname} \n'
                   f'Средняя оценка за лекции: {self.__average_grades()} \n')
        return message

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('Ошибка')

    def __str__(self):
        message = (f'Проверяющий: \n'
                   f'Имя: {self.name} \n'
                   f'Фамилия: {self.surname} \n')
        return message
 
first_student = Student('Василий', 'Петров', 'мужской')
first_student.courses_in_progress += ['Python']
first_student.add_courses('GIT')

second_student = Student('Лиза', 'Иванова', 'женщина')
second_student.courses_in_progress += ['GIT']
second_student.add_courses('Python')

first_lecture = Lecturer('Дмитрий', 'Сидоров')
first_lecture.courses_attached += ['Python']
second_lecture = Lecturer('Семен', 'Рыбанов')
second_lecture.courses_attached += ['GIT']

first_reviewer = Reviewer('Никита', 'Круглов')
first_reviewer.courses_attached += ['Python']
second_reviewer = Reviewer('Петр', 'Чижов')
second_reviewer.courses_attached += ['GIT']

first_student.grades_lecture(first_lecture, 'Python', 10)
first_student.grades_lecture(first_lecture, 'Python', 9)
second_student.grades_lecture(second_lecture, 'GIT', 8)
second_student.grades_lecture(second_lecture, 'GIT', 9)

first_reviewer.rate_hw(first_student, 'Python', 9)
first_reviewer.rate_hw(first_student, 'Python', 9)
second_reviewer.rate_hw(second_student, 'GIT', 6)
second_reviewer.rate_hw(second_student, 'GIT', 10)

# print(first_student)
# print(second_student)
# first_student.__lt__(second_student)
# print(first_lecture)
# print(second_lecture)
# first_lecture.__lt__(second_lecture)
# print(first_reviewer)
# print(second_reviewer)

students = []
students.append(first_student)
students.append(second_student)
#print(students)
name_course = 'Python'
def average(students, course):
    sum_ = 0
    num_course = []
    #for stud in students:
    for name, grades in students.grades.items():
        print(grades)
    #     num_course += grades
    #     length = len(num_course)
    #     for number in grades:
    #         sum_ += number
    # average = sum_ / length
average(students, name_course)
# функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
# (в качестве аргументов принимаем список студентов и название курса);
# функция для подсчета средней оценки за лекции всех лекторов в рамках курса
# (в качестве аргумента принимаем список лекторов и название курса).


# def __average_grades(self):
#     sum_ = 0
#     num_course = []
#     for course, grade in self.grades.items():
#         num_course += grade
#         length = len(num_course)
#         for number in grade:
#             sum_ += number
#     average = sum_ / length
#     return round(average, 2)
# queries = [
#   'смотреть сериалы онлайн',
#   'новости спорта',
#   'афиша кино',
#   'курс доллара',
#   'сериалы этим летом',
#   'курс по питону',
#   'сериалы про спорт'
# ]
#
# qu = {}
# numbers_q = len(queries)
# print(f'Всего запросов: {numbers_q}', '\n')
# for result in queries:
#   result = len(result.split(' '))
#   if result not in qu.keys():
#     qu[result] = 1
#   else:
#     qu[result] += 1
#
# for f, d in qu.items():
#   print(f'Запросов с {f} словами {int(d*100/numbers_q)} %')