#jerelyn
#10-29-2024
#CFU12
def version1():
    password = "simonsnyc"
    userInput = input("enter password: ")
    
    while password != userInput :
        print("wrong password!")
        userInput = input("enter password: ")
print("correct ! you may enter... ")
version1()


def version2():
    password = "simonsnyc"
    userInput = input("enter password: ")
    num_guesses = 0
    
    while password != userInput and num_guesses < 3:
        print("wrong password!")
        userInput = input("enter password: ")
        num_guesses +=1
        
    if password == "simonsnyc":
        print("correct! you may enter...")
    else:
        print("wrong password!")
version2()
