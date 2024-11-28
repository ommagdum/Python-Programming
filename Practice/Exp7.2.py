'''Write a program that has a class Person with data members Name, Age
and Gender. Inherit a class Faculty with data members Designation
and Department from Person which also has a class Publications with
data members Number of research publications. Number of Books,
Number of Articles.'''

class Person:
    def __init__(self, Name, Age, Gender):
        self.name = Name
        self.age = Age
        self.gender = Gender

    def display_person(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")

class Faculty(Person):
    def __init__(self, Name, Age, Gender, Designation, Department,  NumResearch, NumBooks, NumArticles):
        super().__init__(Name, Age, Gender)
        self.designation = Designation
        self.department = Department
        self.publications = Publications(NumResearch, NumBooks, NumArticles)

    def display_faculty(self):
        self.display_person()
        print(f"Designation : {self.designation}")
        print(f"Department : {self.department}")
        self.publications.display_pub()


class Publications:
    def __init__(self, NumResearch, NumBooks, NumArticles):
        self.researchPub = NumResearch
        self.books = NumBooks
        self.articles = NumArticles

    def display_pub(self):
        print(f"Number of Research Publications : {self.researchPub}")
        print(f"Number of Books : {self.books}")
        print(f"Number of Articles : {self.articles}")
    
faculty_member = Faculty(Name="Om Magdum", Age=20, Gender="Male", Designation="Asst. Prof.", Department='CSE', NumResearch=1, NumArticles=2, NumBooks=1)
faculty_member.display_faculty()