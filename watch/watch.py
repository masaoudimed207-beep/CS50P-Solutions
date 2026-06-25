import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if not re.search(r"iframe",s,re.IGNORECASE):
        return None
    url=r'src="https?://(www\.)?youtube\.com/embed/([\w-]+)"'

    if matches:=re.search(url,s):
        return f"https://youtu.be/{matches.group(2)}"
    else:
        return None



if __name__ == "__main__":
    main()
