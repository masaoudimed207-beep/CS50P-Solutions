mon_dict = {}
while True:
    try:
        grocery = input(" ").lower()

        if grocery in mon_dict:
            mon_dict[grocery] += 1
        else:
            mon_dict[grocery] = 1
    except EOFError:
        print()
        for i in sorted(mon_dict.keys()):
            quantity = mon_dict[i]
            print(f"{quantity} {i.upper()}")

        break
