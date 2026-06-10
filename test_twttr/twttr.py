def main():
    tweet=str(input("Input: "))
    vowels="aeiouAEIOU"
    output=""
    for char in tweet:
        if char not in vowels:
            output+=char
    print("Output:",output)
    
if __name__ == "__main__":
    main()