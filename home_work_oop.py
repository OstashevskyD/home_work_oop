class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

harry_potter = Student('Гарри', 'Поттер', 'м')
harry_potter.finished_courses = ['Уход за магическими существами', 'Травология']
harry_potter.courses_in_progress = ['Зельеварение', 'Защита от темных искусств']
harry_potter.grades = {'Уход за магическими существами': 10, 'Травология': 7,
                       'Зельеварение': 10, 'Защита от темных искусств': 1}

ron_wesley = Student('Рон', 'Уизли', 'м')
ron_wesley.finished_courses = ['Уход за магическими существами', 'Травология']
ron_wesley.courses_in_progress = ['Зельеварение', 'Защита от темных искусств']
ron_wesley.grades = {'Уход за магическими существами': 10, 'Травология': 7,
                       'Зельеварение': 10, 'Защита от темных искусств': 1}

hermione_granger = Student('Гермиона', 'Грейнджер', 'ж')
hermione_granger.finished_courses = ['Уход за магическими существами', 'Травология']
hermione_granger.courses_in_progress = ['Зельеварение', 'Защита от темных искусств']
hermione_granger.grades = {'Уход за магическими существами': 10, 'Травология': 10,
                           'Зельеварение': 9, 'Защита от темных искусств': 5}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}

    def ever_grade_lecturer(self, lecturer, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_attached:
            if course in lecturer.grades:
                ever_grade = (grades[0] + grades[1] + grades[2]) \ len(grades)

horace_slughorn = Lecturer('Гораций', 'surname')
horace_slughorn.courses_attached = 'Зельеварение'
grades = [10, 9, 3]

pomone_sprout = Lecturer('Помона', 'Стебль')
pomone_sprout.courses_attached = 'Травология'
pomone_sprout.grades = [10, 10, 10]

dolores_ubridge = Lecturer('Долорес', 'Амбридж')
dolores_ubridge.courses_attached = 'Защита от темных искусств'
dolores_ubridge.grades = [1, 1, 1]

rubeus_hagrid = Lecturer('Рубеус', 'Хагрид')
rubeus_hagrid.courses_attached = 'Уход за магическими существами'
rubeus_hagrid.grades = [10, 10, 10]

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

wilhelmina_grubbly_plunk = Reviewer('Вильгельмина', 'Граббли-Дёрг')
wilhelmina_grubbly_plunk.courses_attached = 'Уход за магическими существами'

severus_snape = Reviewer('Северус', 'Снейп')
severus_snape.courses_attached = 'Зельеварение'

herbert_beery = Reviewer('Герберт', 'Бири')
herbert_beery.courses_attached = 'Травология'

albus_dumbledore = Reviewer('Альбус', 'Дамблдор')
albus_dumbledore.courses_attached = 'Защита от темных искусств'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

def __str__(Student):
    return f'{self.name}, {self.surname}, {self.gender}, ' \
           f'{self.grades}, {self.finished_courses}, {self.courses_in_progress}'
print(Student)


student_list = [
    {'name': 'Гарри', 'surname': 'Поттер', 'gender': 'м',
     'grades': {'Уход за магическими существами': 10, 'Травология': 7,
     'Зельеварение': 10, 'Защита от темных искусств': 1},
     'finished_courses': ['Уход за магическими существами', 'Травология'],
     'courses_in_progress': ['Зельеварение', 'Защита от темных искусств']},
    {'name': 'Рон', 'surname': 'Уизли', 'gender': 'м',
     'grades': {'Уход за магическими существами': 10, 'Травология': 5,
     'Зельеварение': 6, 'Защита от темных искусств': 1},
     'finished_courses': ['Уход за магическими существами', 'Травология'],
     'courses_in_progress': ['Зельеварение', 'Защита от темных искусств']},
    {'name': 'Гермиона', 'surname': 'Грейнджер', 'gender': 'ж',
     'grades': {'Уход за магическими существами': 10, 'Травология': 10,
     'Зельеварение': 9, 'Защита от темных искусств': 5},
     'finished_courses': ['Уход за магическими существами', 'Травология'],
     'courses_in_progress': ['Зельеварение', 'Защита от темных искусств']}
    ]


lecturer_list = [
    {'name': 'Гораций', 'surname': 'Слизнорт', 'courses_attached': 'Зельеварение',
     'grades': [10, 9, 3]},
    {'name': 'Помона', 'surname': 'Стебль', 'courses_attached': 'Травология',
     'grades': [10, 10, 10]},
    {'name': 'Долорес', 'surname': 'Амбридж', 'courses_attached': 'Защита от темных искусств',
     'grades': [1, 1, 1]},
    {'name': 'Рубеус', 'surname': 'Хагрид', 'courses_attached': 'Уход за магическими существами',
     'grades': [10, 10, 10]}
]

reviewer_list = [
    {'name': 'Вильгельмина', 'surname': 'Граббли-Дёрг', 'courses_attached': 'Уход за магическими существами'},
    {'name': 'Северус', 'surname': 'Снейп', 'courses_attached': 'Зельеварение'},
    {'name': 'Герберт', 'surname': 'Бири', 'courses_attached': 'Травология'},
    {'name': 'Альбус', 'surname': 'Дамблдор', 'courses_attached': 'Защита от темных искусств'}
]
