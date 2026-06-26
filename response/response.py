from validator_collection import validators
def main():
    print(validate(input("What's your email address? ")))

def validate(s):
    try:
        if validators.email(s):
            return "Valid"
    except ValueError:
        return "Invalid"
    
if __name__=="__main__":
    main()