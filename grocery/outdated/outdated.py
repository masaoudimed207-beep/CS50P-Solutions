while True:
    try:
        months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        date = input("Date: ").strip()

        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)

            if 1 <= month <= 12 and 1 <= day <= 31:
                
                print(f"{year:04}-{month:02}-{day:02}")
                break

        elif "," in date:
            parts = date.split(" ")
            if len(parts) == 3:
                month_name = parts[0].title()  
                day_str = parts[1].replace(",", "")  
                year = int(parts[2])
                if month_name in months:
                    month = months.index(month_name) + 1
                    day = int(day_str)

                    if 1 <= day <= 31:

                        print(f"{year:04}-{month:02}-{day:02}")
                        break

    except ValueError:
        continue
