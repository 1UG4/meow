leiviskät = float(input("leiviskät: "))
naulat = float(input("naulat: "))
luodit = float(input("luodit: "))


yhteensa_luodit = (leiviskät * 20 * 32) + (naulat * 32) + luodit
yhteensä_grammat = yhteensa_luodit * 13.3

kilogrammat = int(yhteensä_grammat // 1000)
grammat = yhteensä_grammat % 1000

print("massa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")
