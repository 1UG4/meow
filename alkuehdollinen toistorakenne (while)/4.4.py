import random
luku = random.randint (1,10)
arvaus = 0
while arvaus != luku:
    arvaus = int(input("Anna arvaus: "))
    if arvaus < luku:
        print("liian pieni arvaus yritä uudestaan")
    elif arvaus > luku:
        print("liian iso luku")
    elif arvaus == luku:
        print("nappiin meni")