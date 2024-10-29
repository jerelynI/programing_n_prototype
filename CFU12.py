#jerelyn
#10-29-2024
#CFU12
correct_password = "simonsnyc"
while True:
    user_password = input("Please enter the password: ")
    if user_password == correct_password:
        print("Correct! You may enter..")
        break  
    else:
        print("Wrong Password!")
