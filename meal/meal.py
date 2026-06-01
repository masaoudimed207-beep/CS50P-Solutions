def main():
    time=input("What time is it? ")
    t=convert(time)
    if 7.00 <= t <= 8.00:
        print("breakfast time")
    elif 12.00 <= t <= 13.00:
        print("lunch time")
    elif 18.00 <= t <= 19.00:
        print("dinner time")
    


def convert(time):
    hour,minute=time.strip().split(":")
   
    return float(hour) + float(minute)/60


if __name__ == "__main__":
    main()