# Enter age from user and if age<18, print message as “Not Eligible for voting”, with user defined exception
class NotEligibleForVotingError(Exception):
    """Custom exception raised when the age is below 18."""
    pass

def check_voting_eligibility():
    try:
        age = int(input("Enter your age: "))
        if age < 18:
            raise NotEligibleForVotingError("Not Eligible for voting")
        else:
            print("Eligible for voting")
    except NotEligibleForVotingError as e:
        print(e)
    except ValueError:
        print("Invalid input. Please enter a valid integer for age.")

# Run the function
check_voting_eligibility()