
def dataInput(list, n):
    for i in range(n):
        p = input().split(",") #name, sex, height[cm], mass[kg], age
        list.append(p)
    return None

#BMI index = mass(kg)/height(m)^2
def bmi(p):
    return float(p[3])/(float(p[2])/100)**2

def printPerson(p):
    print("Name: {}\nSex: {}\nHeight[cm]: {}\nMass[kg]: {}\nAge: {}\n!BMI index: {:.2f}\n".format(p[0], p[1], p[2], p[3], p[4], bmi(p)))

def categories(people, min, max):
    kat = [0, 0, 0, 0]
    for i in range(len(people)):
        if min <= int(people[i][4]) <= max:
            p = bmi(people[i])
            if p < 18.5:
                kat[0] += 1
            elif p < 25:
                kat[1] += 1
            elif p < 30:
                kat[2] += 1
            else:
                kat[3] += 1
    print("Number of people in each category:")
    print("UNDERWEIGHT: {0}\nIDEAL MASS: {1}\nOVERWEIGHT: {2}\nOBESITY: {3}".format(kat[0], kat[1], kat[2], kat[3]))
    return

n = int(input())
if n < 0:
    pass
else:
    rangeY = input().split("-")
    people = []
    dataInput(people, n)
    for i in range(n):
        printPerson(people[i])
        #print("{} {} {} {:.2f}".format(people[i][0], people[i][1], people[i][4], bmi(people[i])))
    categories(people, int(rangeY[0]), int(rangeY[1]))