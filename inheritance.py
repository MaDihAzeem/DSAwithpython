#inheritance
class person:
    def person_info(self,name,age):
        print(name,age)

class company:
    def company_info(self,company_name,location):
        print(company_name,location)
class employee(person,company):
    def employee_info(self,designation,skill,salary):
        print(designation,skill,salary)


name=input("enter your name:")
age=int(input("enter your age:"))
company_name=input("enter yor caompany:")        
location=input("enter location:")
designation=input("enter your designation:")
skill=input("enter your skill")
salary=int(input("enter your salary"))
emp=employee()
emp.person_info(name,age)
emp.company_info(company_name,location)
emp.employee_info(designation,skill,salary)

