class SchoolMember:
    """Represents a school member"""

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("(Initialized School Member): {}".format(self.name))

    def tell(self):
        """Tell details"""
        print("Name: {}, Age: {}".format(self.name, self.age, end=" "))


class Teacher(SchoolMember):
    """Represents a teacher"""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("Initialized teacher: {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Salary: {:d}".format(self.salary))


class Student(SchoolMember):
    """Represents a student"""

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("Initialized student: {}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Marks: {:d}".format(self.marks))


t = Teacher('Mr. Shahjahan', 60, 30000)
s = Student('Soikat', 10, 80)

t.tell()
s.tell()
