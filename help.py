import random
otvet = random.randint(1, 5)
x = int(input("dai chislo: "))
if otvet == x:
    print("good job")
else:
    print("no (")
    print(otvet)

