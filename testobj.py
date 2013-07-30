class Person:
    def intruduceself(self):
        print self.name,self.age
    def __init__(self,name = "test",age = 18):
        self.name = name
        self.age = age
xiaoming = Person()
xiaoming.intruduceself()
xiaohong = Person("hong",14)
Person.intruduceself(xiaohong);
