import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    pattern = r"^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    matches = re.search(pattern, s)
    
    if not matches:
        raise ValueError
        
    h1 = int(matches.group(1))
    m1 = int(matches.group(2)) if matches.group(2) else 0
    p1 = matches.group(3)
    
    h2 = int(matches.group(4))
    m2 = int(matches.group(5)) if matches.group(5) else 0
    p2 = matches.group(6)
    
    
    if h1 > 12 or h2 > 12 or m1 >= 60 or m2 >= 60:
        raise ValueError

    if p1 == "PM" and h1 != 12:
        h1 += 12
    elif p1 == "AM" and h1 == 12:
        h1 = 0
        
    if p2 == "PM" and h2 != 12:
        h2 += 12
    elif p2 == "AM" and h2 == 12:
        h2 = 0

    
    return f"{h1:02d}:{m1:02d} to {h2:02d}:{m2:02d}"

if __name__ == "__main__":
    main()