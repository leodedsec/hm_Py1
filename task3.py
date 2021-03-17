##class Lecturer():
##    def __init__(self,name,surname):
##        self.name=name
##        self.surname=surname
##    def __str__(self):
##        return self.name, self.surname
##
##lector=Lecturer("Leo", "Messi")
##print(lector)

grades={"a":4,"b":6}
print(sum(grades.values())/len(grades))


class Test():
    def kek(self):
        get=input()
        self.grades=[]
        self.grades.append(get)
a=Test()
a.kek()
print(a.grades)