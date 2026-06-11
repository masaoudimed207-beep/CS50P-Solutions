def main():
    while True:
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
            output = gauge(percentage)
            print(output)
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):

    if "/" not in fraction:
        raise ValueError
    
    x_str, y_str = fraction.split("/")
    
    
    if not x_str.isdigit() or not y_str.isdigit():
        raise ValueError
        
    x = int(x_str)
    y = int(y_str)
    
    
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
        
    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
