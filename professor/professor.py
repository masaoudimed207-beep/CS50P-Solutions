import random
from tabnanny import check
def main():
    level=get_level()
    counter=0
    for i in range(10):
        x=generate_integer(level)
        y=generate_integer(level)
        tries=0
        while True:       
            try:
                n=input(f"{x} + {y} = ")
                if int(n)==x+y:
                    counter+=1
                    break
                else:
                    print("EEE")
                    tries+=1
            except ValueError:
                print("EEE")
                tries+=1
            if tries==3:
                print(f"{x} + {y} = {x+y}")
                break
    print(f"Score: {counter}")
                
        
def get_level():
    while True:
        try:
            n=int(input("Level: "))
            if n>0 and n<=3:
                return n
        except ValueError:
            continue
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
        

if __name__=="__main__":
    main()