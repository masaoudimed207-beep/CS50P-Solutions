import re 
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    condition=r"(25[0-5]|2[0-4]\d|1\d{2}|\d{1,2})"
    pattern=r"^"+condition+r"\."+condition+r"\."+condition+r"\."+condition+r"$"
    
    if re.search(pattern, ip):
        return True
    else:
        return False 
    
if __name__=="__main__":
    main()