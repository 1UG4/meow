OIKEA_TUNNUS = "python"
OIKEA_SALASANA = "rules"
yritykset = 0

while True:
    tunnus = input("anna tunnus: ")
    salasana = input("anna salasana: ")

    if tunnus == OIKEA_TUNNUS and salasana == OIKEA_SALASANA:
        print("Tervetuloa")
        break

    yritykset += 1

    if yritykset == 5:
        print("Pääsy evätty")
        break