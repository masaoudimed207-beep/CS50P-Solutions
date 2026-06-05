while True:
    try:
        flue=input("Fraction: ")
        x,y=flue.split("/")
        x=int(x)
        y=int(y)
        result=round(x/y*100)
        if x>y or x<0 or y<=0:
            continue
        if result>=99:
            output="F"
        elif result<=1:
            output="E"
            
        else:
            output=f"{result}%"
        
    except (ValueError, ZeroDivisionError):
        pass
    else:
        print(output)
        break
   
        