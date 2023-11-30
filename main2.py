#Python Object-Oriented Programming

class Employee:
    def __init__(self,first,last,pay):   #use init method , but when we do all ,we pass first here
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first + '.' + last + '@yakku.com'
        

emp_1 = Employee('Fahmi','Zainal','5000')
emp_2 = Employee('Safwan','Ali','5000')

print(emp_1)
print (emp_2)

Instance Variables Variables and their input to it
emp_1.first = 'Fahmi'
emp_1.last = 'Zainal'
emp_1.email = 'Fahmi.Zainal@yakku.com'
emp_1.pay = 5000

emp_2.first = 'Safwan'
emp_2.last = 'Ali'
emp_2.email = 'Safwan.Ali@yakku.com'
emp_2.pay = 5000

print(emp_1)
print(emp_2)


print(emp_1.email)
print(emp_2.email)

print(emp_2.fullname())
print(emp_1.fullname())
