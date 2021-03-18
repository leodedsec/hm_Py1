class Student:
    def __str__(self):
        self.globalGrades=[]
        #т.к оценки хранятся в виде ключ-[оценки], т.е нужно вытащить оценки, чтобы работать с ними
        def replaceGrades():
            for i in self.grades.values():
                for j in i:
                   self.globalGrades.append(j)
        replaceGrades()
        return f"Имя: {self.name}\nФамилия: {self.surname}\n\
Средняя оценка за домашние задания: {sum(self.globalGrades)/len(self.globalGrades)}\n\
Курсы в процессе изучения: {self.courses_in_progress}\n\
Завершенные курсы: {self.finished_courses}"
    def __lt__(self, other):
        return sum(self.globalGrades)/len(self.globalGrades)<sum(other.globalGrades)/len(other.globalGrades)
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [] #Полностью решенные и проверенные учителем курсы
        self.courses_in_progress = [] #Курсы на проверку
        self.grades = {} #Оценки
    #поставить оценку лектору
    def gradeLecturer(self,lector):
        rangeGrades=[int(i) for i in range(11)] #оценки 0-10
        getLecurer=list(map(str, input("Имя/Фамилия лектора:").split()))
        if getLecurer[0]==lector.name and getLecurer[1]==lector.surname:
            for i in self.courses_in_progress:
                if i in lector.courses_attached:
                    get_grade=None
                    while get_grade not in rangeGrades:
                        get_grade=int(input("Оценка лектору: "))
                    lector.grade_lecturer.append(get_grade)
                    break
            else:
                print("Наборы курсов у преподавателя/ученика разнятся!")
        else:
            print("Такого лектора не сущесвует в нашем вузе!")



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = [] #Список доступных курсов на проверку
        self.grade_lecturer=[]


#Проверяющие ДЗ
class Reviewers(Mentor):
    def __str__(self):
        return "Имя: "+self.name+"\n"+"Фамилия: "+self.surname
    def rate_hw(self, student, course, grade):
        #Если экземпляр класса относится к классу Student
        #и если курс имеется у проверяющего and студента на проверке
        if isinstance(student, Student) and course in self.courses_attached\
        and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"


#Лекторы, которым студенты ставят оценки
class Lecturer(Mentor):
    def __str__(self):
        return "Имя: "+self.name+"\n"+"Фамилия: "+self.surname+"\n"+\
        "Средняя оценка за лекции: "+str(sum(self.grade_lecturer)/len(self.grade_lecturer))
    def __lt__(self, other):
        return sum(self.grade_lecturer)/len(self.grade_lecturer) < sum(other.grade_lecturer)/len(other.grade_lecturer)
    def addCourses(self):
        get_course=input("Введите название курса:")
        self.courses_attached.append(get_course)



lector1=Lecturer("O","N") #создали лектора
lector1.addCourses() #добавили курс лектору 1

lector2=Lecturer("O","M")
lector2.addCourses() #добавили курс лектору 2

pupil1=Student("Azat","Abdrashitov","M") #создали студента 1
pupil1.courses_in_progress.append("GIT") #добавили курс студенту 1
pupil1.courses_in_progress.append("Python") #добавили курс студенту 1
pupil1.finished_courses.append("English") # добавили завершенный курс
pupil1.gradeLecturer(lector1) #оценка1 лектору 1 --
pupil1.gradeLecturer(lector1) #оценка2 лектору 1 -- --=>все от студента1
pupil1.gradeLecturer(lector2) #оценка1 лекетору2 --


pupil2=Student("Leo","Messi","M") #создали студента 2
pupil2.courses_in_progress.append("GIT") #добавили курс студенту 2
pupil2.courses_in_progress.append("Python") #добавили курс студенту 2
pupil2.finished_courses.append("None") # добавили завершенный курс
pupil2.gradeLecturer(lector2) #оценка1 лектору2 от студента2


homework1=Reviewers("Boris","Trushin") #создали проверяющего 1
homework1.courses_attached.append("GIT") #добавили курс проверяющему 1
homework1.courses_attached.append("Python") #добавили курс проверяющему 1
homework1.rate_hw(pupil1,"GIT",7) #поставили оценку 7 студенту1
homework1.rate_hw(pupil1,"Python",3) #поставили оценку 3 студенту1
homework1.rate_hw(pupil1,"Python",2) #поставили оценку 2 студенту1
homework1.rate_hw(pupil2,"GIT",3) #поставили оценку 3 студенту
homework1.rate_hw(pupil2,"Python",5)



def gradesStudents(*args,course=""):
    countGrades=[]
    for student in args:
        if course in student.grades:
            countGrades+=student.grades[course]
    print(f"Средняя оценка студентов: {[i.name for i in args]}\
    по курсу: {course} == {sum(countGrades)/len(countGrades)}")

gradesStudents(pupil1,pupil2,course="Python")


def gradesLecturers(*args,course=""):
    countGrades=[]
    for lector in args:
        if course in lector.courses_attached:
            countGrades+=lector.grade_lecturer
    print(f"Средняя оценка лекторов: {[i.name for i in args]}\
    по курсу: {course} == {sum(countGrades)/len(countGrades)}")

gradesLecturers(lector1,lector2,course="GIT")



print(lector1) #Инфа о лекторе1
print()
print(lector2) #Инфа о лекторе2
print()
print(homework1) #Инфа о проверяющем1
print()
print(pupil1) #Инфа о студенте1
print()
print(pupil2) #Инфа о студенте2
print()

#Сравнение
a=pupil2<pupil1
if a==False:
    print(">")
else:
    print("<")

b=lector1<lector2
if b==False:
    print(">")
else:
    print("<")


