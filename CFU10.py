import random


def guess_the_number():
   
    random_number = random.randint(1, 10)
    
    
    attempts = 0
    
    while True:
       
        guess = int(input("Guess a number between 1 and 10: "))
        
       
        attempts += 1
        
      
        if guess == random_number:
          
            print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
            break
        else:
          
            if guess > random_number:
               
                print("Too High!")
            else:
               
                print("Too Low!")

guess_the_number()
