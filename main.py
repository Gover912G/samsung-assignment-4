#Grading system program

mat = int(input("Enter your mathematics score:"))
physics = int(input("Enter your physics score:"))
geo = int(input("Enter your geo score:"))
Chem = int(input("Enter your Chem score:"))

scores = [mat,physics,geo,Chem]
for x in scores:
    if x <= 0 or x >= 100:
        print("score cant be negative")
        break

def add( scores):
    total = 0
    for x in scores:
        total +=x
        return total
def average():

    ave = add(scores)/len(scores)

    return ave


if average() > 70:
    print("A")
elif average() >60 and average() == 70:
    print("B")
elif average() ==50 and average() < 60:
    print("C")
elif average() ==40 and average() <50:
    print("D")
elif average() < 40:
    print("E")
else:
    print("")

print(average())

