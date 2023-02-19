class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {"Python": [10, 10, 10, 10], "Java": [8, 8, 8, 8]}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, mentor, course, grade):
        if isinstance(mentor, Lecturer) and course in self.courses_in_progress and course in mentor.courses_attached:
            if course in mentor.grades:
                mentor.grades[course] += [grade]
            else:
                mentor.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_avg(self):
        self.numbers = []
        for key, value in self.grades.items():
            for number in value:
                self.numbers.append(number)
        res = sum(self.numbers) / len(self.numbers)
        return res

    def __str__(self):
        res = f'Имя: {self.name}' \
              f'\nФамилия: {self.surname}' \
              f'\nСредняя оценка за домашние задания: {self.avr()}' \
              f'\nКурсы в процессе обучения: {", ".join(self.courses_in_progress)}' \
              f'\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.get_avg() < other.get_avg()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {"Python": [10, 10, 10, 10], "Java": [8, 8, 8, 8]}

    def get_avg(self):
        self.numbers = []
        for key, value in self.grades.items():
            for number in value:
                self.numbers.append(number)
        res = sum(self.numbers) / len(self.numbers)
        return res

    def __str__(self):
        res = f'Имя: {self.name} ' \
              f'\nФамилия: {self.surname} ' \
              f'\nСредняя оценка за лекции: {self.get_avg()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.get_avg() < other.get_avg()


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} ' \
               f'\nФамилия: {self.surname}'


# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)

a = Lecturer("Игорь", "Student")
print(a)
