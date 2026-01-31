def voter(age):
    if age < 18:
        raise ValueError ("Invalid Voter")
    return("You are allowed to vote ")
try:
    print(voter (18))
except ValueError as e:
    print (e)