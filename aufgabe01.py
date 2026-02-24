start = int(input("Startwert: "))
ende  = int(input("Endwert: "))

a = []

for i in range(start,ende):
    if(i%2==0):
        a.append(i)

print(a)