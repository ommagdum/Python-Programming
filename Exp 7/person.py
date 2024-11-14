# Write a program that has a class Person with data members Name, Age and Gender. 
# Inherit a class Faculty with data members Designation and Department from Person which also has a class Publications with data members Number of research publications. 
# Number of Books, Number of Articles. 

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")


class Publications:
    def __init__(self, num_research_papers, num_books, num_articles):
        self.num_research_papers = num_research_papers
        self.num_books = num_books
        self.num_articles = num_articles

    def display_publications_info(self):
        print(f"Research Publications: {self.num_research_papers}")
        print(f"Books: {self.num_books}")
        print(f"Articles: {self.num_articles}")


class Faculty(Person):
    def __init__(self, name, age, gender, designation, department, num_research_papers, num_books, num_articles):
        super().__init__(name, age, gender)
        self.designation = designation
        self.department = department
        # Aggregation of Publications
        self.publications = Publications(num_research_papers, num_books, num_articles)

    def display_faculty_info(self):
        self.display_person_info()
        print(f"Designation: {self.designation}")
        print(f"Department: {self.department}")
        self.publications.display_publications_info()


# Example usage
faculty_member = Faculty(
    name="Dr. Alice Smith",
    age=45,
    gender="Female",
    designation="Professor",
    department="Computer Science",
    num_research_papers=20,
    num_books=3,
    num_articles=10
)

# Display information
faculty_member.display_faculty_info()