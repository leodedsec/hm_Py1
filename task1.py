class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [] #Полностью решенные и проверенные учителем курсы
        self.courses_in_progress = [] #Курсы, которые решил студент, но еще не проверены
        self.grades = {} #Оценки


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        #Список курсов, которые может проверить учитель
        self.courses_attached = []


class Reviewers(Mentor):
    def rate_hw(self, student, course, grade):
        #Если экземпляр класса относится к классу Student и если курс имеется у учителя/студента на проверке
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"



def main():
    userInput=""
    while userInput!="q":
        print("""
                1 - Внести информацию о студенте
                2 - Проверить работу студента
                3 - Поставить оценку лектору за лекцию
                q - Exit
    """)
        userInput=input("Выбор:")
        if userInput=="1":
            name=input("Имя студента:")
            surname=input("Фамилия студента:")
            male=input("Пол студента:")
            pupil=Student(name,surname,male)
            addCourse=input("Студент предоставил на проверку курс:")
            pupil.courses_in_progress.append(addCourse)
            print(f"Информация об ученике:\n\
                    Имя: {pupil.name}\n\
                    Фамилия: {pupil.surname}\n\
                    Отдал курс на проверку: {pupil.courses_in_progress}")
        elif userInput=="2":
            name=input("Имя учителя:")
            surname=input("Фамилия учителя:")
            course=input("Курс на проверку:")
            grade=int(input("Оценка за курс:"))
            reviewers=Reviewers(name,surname)
            reviewers.rate_hw(pupil,course,grade)
            reviewers.courses_attached.append(course)
            print(f"Информация об учителе:\n\
                    Имя: {name}\n\
                    Фамилия: {surname}\n\
                    За курс {course} была поставлена оценка {pupil.grades[course]}")
        elif userInput=="q":
            print("Exit...")
    print(pupil.name,pupil.surname)
    print()

main()
