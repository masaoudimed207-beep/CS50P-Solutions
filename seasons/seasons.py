from datetime import date
import sys 
import inflect

def main():
    birthday=input("Date of birth: ")
    print(Switch(birthday))
    

class Switch:
    def __init__(self,date_str):
        try:
            self.birth_date=date.fromisoformat(date_str)
        except ValueError:
            sys.exit("Invalid date")
            
        self.today=date.today()
        diff_day=(self.today - self.birth_date).days
        self.minutes=diff_day*24*60
        
    def __str__(self):
        p=inflect.engine()
        words=p.number_to_words(self.minutes,wantlist=False)
        words=words.replace(" and ", " ")
        return f"{words.capitalize()} minutes"

if __name__ == "__main__":
    main()