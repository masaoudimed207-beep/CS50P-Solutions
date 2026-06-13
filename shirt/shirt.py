import sys
import os
from PIL import Image, ImageOps

def main():
    
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
        
    ext1 = os.path.splitext(sys.argv[1])[1].lower()
    ext2 = os.path.splitext(sys.argv[2])[1].lower()
    
    
    valid_extensions = [".jpg", ".jpeg", ".png"]
    if ext1 not in valid_extensions:
        sys.exit("Invalid input")
        
    
    if ext1 != ext2:
        sys.exit("Input and output have different extensions")
        

    try:

        shirt = Image.open("shirt.png")  
        user_image = Image.open(sys.argv[1])
        user_image = ImageOps.fit(user_image, shirt.size)
        user_image.paste(shirt, shirt)
        user_image.save(sys.argv[2])
        
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()