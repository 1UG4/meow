kuha = int(input("Anna kuhan pituus senttimetreinä: "))

if kuha < 37:
    puuttuu = 37 - kuha
    print(f"Laske kuha takaisin järveen! Alimmasta sallitusta pyyntimitasta puuttuu {puuttuu} cm.")
else:
    print("Vittu mikä vonkale!")