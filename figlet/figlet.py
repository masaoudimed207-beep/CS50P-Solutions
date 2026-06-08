import sys 
import random
from pyfiglet import Figlet
figlet=Figlet()

if len(sys.argv)==1:
    font=random.choice(figlet.getFonts())
    figlet.setFont(font=font)
elif len(sys.argv)==3 and (sys.argv[1]=="-f" or sys.argv[1]=="--font") and sys.argv[2] in figlet.getFonts():
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")

    
text=input("Input: ")
print(figlet.renderText(text))
        
        