while True:
    tuumat = float(input("tuumat: "))
    if tuumat < 0:
        print("ohjelma lopetettu")
        break
    cm = tuumat * 2.54
    print(f"{tuumat} tuumaa on {cm} senttimetriä")
