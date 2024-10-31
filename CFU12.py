#jerelyn
#10-29-2024
#CFU12
def v1():
    password = "simonsnyc"
    userInput = input("enter password: ")
    
    while password != userInput :
        print("wrong password!")
        userInput = input("enter password: ")
        
    print("correct ! you may enter... ")

#v1()
def v2():
    password = "simonsnyc"
    userInput = input("Enter passcode:")
    i = 0
    while password != userInput and i < 3:
        print("wrong password!")
        i+=1
        userInput = input("Enter passcode: ")
        if password == userInput:
            print("correct! You may Enter...")
            
#v2()
def main():
    version = input("choose 1 or 2")
    if version == "1":
        v1()
    elif version == "2":
        v2()
    else:
        print("that isnt a choice")

main()
