class Person:
    def __init__(self,name,gender,profession):
        self.name=name
        self.gender=gender
        self.profession=profession

    def show(self):
        print("Name",self.name,"Gender",self.gender)   

    def work(self):
        print(self.name,"working as a",self.profession) 

name=input("enter your name")
gender=input("enter your gender")
profession=input("enter your profession")

n1=Person(name,gender,profession)
n1.show()
n1.work()

