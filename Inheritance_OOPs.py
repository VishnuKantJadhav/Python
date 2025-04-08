"""

INHERITANCE :
            Inheritance is a mechanism where a class (child/subclass) inherits the
            properties and behaviors (methods) from another class (parent/superclass).

Composition :
            Composition is a design principle where one class contains an object of
            another class to reuse its functionality.

"""

"""

class Person:

    def __init__(self, name, qual, gen):
        self.name = name
        self.qual = qual
        self.gen = gen

    def pdetails(self):
        print("name of the persion is : ", self.name)
        print("Qualification of the persion : ", self.qual)
        print("Gender of the persion : ", self.gen)

    def status(self):
        print(f"{self.name} is single")


class Student(Person):

    def __init__(self, name, qual, gen, branch, clg, prc, emp):
        super().__init__(name, qual, gen)
        self.branch = branch
        self.clg = clg
        self.prc = prc
        self.emp = emp

    def sinfo(self):
        self.pdetails()
        self.status()
        print(f"College of the {self.name} is : ", self.clg)
        print(f"Branch of the {self.name} is : ", self.branch)
        print(f"percentage of the {self.name} is : ", self.prc)
        print(f"{self.name} got job ")
        self.emp.edetails()


class Employee:

    def __init__(self, eid, desig, sal):
        self.eid = eid
        self.desig = desig
        self.sal = sal

    def edetails(self):

        print(f"Employee ID of Employee : ", self.eid)
        print(f"Designation of Employee : ", self.desig)
        print(f"Salary of Employee : ", self.sal)


emp = Employee("AVD1234", "Intern", 100000)
std = Student("Vishnukant", "MCA", "Male", "CS", "DYP", "71%", emp)
std.sinfo()

"""
"""
Types of Inheritance : 

        1. Single Inheritance
        2. Multi-Level Inheritance
        3. Hirarchical Inheritance
        4. Multiple Inheritance
        5. Hybrid Inheritance

    
    

"""
