#jerelyn
#CFU 17

box = "LoliPop"

def formating(box):
    userInput = int(input("Choice?(1,2,3,4,5,6,7,8,9): "))
   
    if userInput == 1:
       
        print(box.capitalize())
    elif userInput == 2:
       
        position = box.find("i")
        print(position)  
    elif userInput == 3:
       
        print(box.isdigit())  
    elif userInput == 4:
       
        print(box.lower())
    elif userInput == 5:
       
        print(box.replace("o", "a"))
    elif userInput == 6:
       
        print(box.upper())
    else:
        print("Not a valid option")

formating(box)
