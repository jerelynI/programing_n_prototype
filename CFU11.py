def print_numbers():
    for i in range(10, 71, 10):
        print(i)

def print_floats():
    for i in range(0, 201):
        print(i / 2)

def sing_99_bottles_of_beer():
    for i in range(99, 0, -1):
        print(f"{i} bottle{'s' if i > 1 else ''} of beer on the wall, {i} bottle{'s' if i > 1 else ''} of beer.")
        print(f"Take one down, pass it around, {i - 1} bottle{'s' if i - 1 != 1 else ''} of beer on the wall.\n")
    
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")

print_numbers()
print_floats()
sing_99_bottles_of_beer()
