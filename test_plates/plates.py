def main():
    plate=input("Plate:")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if s.isalnum() == False:
        return False
    for i in range(len(s)):
        if s[i].isdigit() == True:
            if s[i] == "0":
                return False
            for j in range(i, len(s)):
                if s[j].isalpha():
                    return False
            return True
    return True

if __name__ == "__main__":
    main()