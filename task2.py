class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [] #Полностью решенные и проверенные учителем курсы
        self.courses_in_progress = [] #Курсы на проверку
        self.grades = {} #Оценки
    def gradeLecturer(self,lector):
        rangeGrades=[int(i) for i in range(11)]
        for i in self.courses_in_progress:
            if i in lector.courses_attached:
                get_grade=None
                while get_grade not in rangeGrades:
                    get_grade=int(input())
                lector.grade_lecturer.append(get_grade)
                break
        else:
            print("Наборы курсов у преподавателя/ученика разнятся!")



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] #Список курсов на проверку


class Reviewers(Mentor):
    def rate_hw(self, student, course, grade):
        #Если экземпляр класса относится к классу Student
        #и если курс имеется у учителя/студента на проверке
        if isinstance(student, Student) and course in self.courses_attached\
        and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"


class Lecturer(Mentor):
    grade_lecturer=[]
    def addCourses(self):
        get_course=input("Введите название курса:")
        return get_course


def main():
    getChoice=None
    while getChoice!="q":
        print("""
            s - add student
            l - add lecturer
            aG - student gives a grade to the lecturer
            aCS - add course to the student
            aCL - add course to the lecturer
            look - print()
            """)
        getChoice=input("Выбор:")
        if getChoice=="s":
            name=input("Имя студента:")
            surname=input("Фамилия студента:")
            gender=input("Гендер студента:")
            pupil=Student(name,surname,gender)
        elif getChoice=="l":
            name=input("Имя лектора:")
            surname=input("Фамилия лектора:")
            teacher=Lecturer(name,surname)
        elif getChoice=="aCS":
            course=input("Добавить курс:")
            pupil.courses_in_progress.append(course)
        elif getChoice=="aCL":
            course=teacher.addCourses()
            teacher.courses_attached.append(course)
        elif getChoice=="aG":
            getLecurer=list(map(str, input("Имя/Фамилия лектора:").split()))
            if getLecurer[0]==teacher.name and getLecurer[1]==teacher.surname:
                pupil.gradeLecturer(teacher)
            else:
                print("Такого лектора не сущесвует!")
        elif getChoice=="look":
            print(pupil.name,pupil.surname)
            print(teacher.name,teacher.surname)
            print(teacher.grade_lecturer)

main()
##teacher1=Lecturer("Oleg","Nazarov")
##a=teacher1.addCourses()
##teacher1.courses_attached.append(a)
##
##pupil1=Student("Azat","Abdrashitov","M")
##b=input("Введите название курса:")
##pupil1.courses_in_progress.append(b)
##pupil1.gradeLecturer(teacher1)
##print(teacher1.grade_lecturer)