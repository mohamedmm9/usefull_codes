class Person:
    def __init__(self, name, year_born):
        self.name = name 
        self.year_born = year_born
    def getAge(slef):
        return CURRENT_Year - slef.year_born
    def __str__(self):
        return '{} ({})'.format(self.name,self.getAge())

alice= Person('Alice',1990)
print(alice)

class Student(Person):
    def __init__(self, name, year_born):
        Person.__init__(self, name, year_born)
        self.knowledge = 0
    def study(self):
        self.knowledge += 1

naruto = Student('naruto',2001)
naruto.getAge()
print(naruto)
