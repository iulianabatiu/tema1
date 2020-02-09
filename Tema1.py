import random
generated=random.randint(0,100)
number=0
while number!=generated:
    number=int(input("Numarul este: "))
    if number<generated:
        print("Caut un numar mai mare")
    elif number>generated:
        print("Caut un numar mai mic")
    else:
        print("Corect")
        