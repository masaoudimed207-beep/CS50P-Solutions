def main():
    greeting = input("Greeting: ")
    # Kat-3yet 3la value() o kat-printi l-flous m9addines
    print(f"${value(greeting)}")


def value(greeting):
    # L-mantiq dyalk d-Semaine 1:
    # 7yed l-espaces o rj3 l-kalma lowercase b- `.lower().strip()`
    greeting = greeting.lower().strip()
    
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
    