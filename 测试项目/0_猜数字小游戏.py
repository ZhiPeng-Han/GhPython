temp = input("Guess what the number is in my mind:")
guess = int(temp)
while guess != 8:
        if guess == 8:
                print("yep!")
                print("amazing!")
        else:
                if guess > 8:
                    print("bigger")
                else:
                    print("smaller")
        temp = input("wrong!Guess what the number is in my mind:")
        guess = int(temp)
print("end^_^")		 
