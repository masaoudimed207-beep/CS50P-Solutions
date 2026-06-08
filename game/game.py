import random

while True:
    try:
        n=int(input("Level: "))
        if n>0:
            break
    except ValueError:
        continue
    

secret=random.randint(1, n)

while True:
    try:
        guess=int(input("Guess: "))
    except ValueError:
        continue
    if guess<=0:
        continue
    if guess<secret:
        print("Too small!")
    elif guess>secret:
        print("Too large!")
    else:
        print("Just right!")
        break  