'''Enter age from user and if age<18, print message as “Not
Eligible for voting”, with user defined exception'''

class NotEligible(Exception):

    def __init__(self, age, message = "Not Eligible For Voting."):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message} Entered Age : {self.age}"
    
def SetAge():
    UserAge = int(input("Enter Your Age : "))
    if UserAge < 18:
        raise NotEligible(UserAge)
    print("You Are Eligible For Voting")

try:
    SetAge()
except NotEligible as e:
    print(f"Error : {e}")
    
