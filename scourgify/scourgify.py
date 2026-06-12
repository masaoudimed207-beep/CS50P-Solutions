import csv 
import sys

if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Could not read file"+sys.argv[1])
    
data1=[]
try:
    
    with open(sys.argv[1]) as file1:
        reader1=csv.DictReader(file1)
        for row in reader1:
            last, first=row["name"].split(",")
            data1.append({"first":first,"last": last,"house":row["house"] })
            
except FileNotFoundError:
    sys.exit("Cloud not read "+sys.argv[1])       
    
with open(sys.argv[2],"w") as file2:
    reader2=csv.DictWriter(file2,fieldnames=["first","last","house"])
    reader2.writeheader()
    reader2.writerows(data1)
        
   

        