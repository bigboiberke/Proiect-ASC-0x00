cheie = input("Parola decriptare: ")
f = open(input("Nume fisier criptat: "), "rb")
g = open(input("Nume fisier pentru decriptare: "), "w")
sir = f.read()
sir = sir.decode("utf-8")
sirnou = ""
j = 0
lungimecheie = len(cheie)
lungimesir = len(sir)
for i in range(lungimesir):
    if j == lungimecheie:
        j = 0
    sirnou = sirnou + chr(ord(sir[i]) ^ ord(cheie[j]))
    j = j+1
try:
    g.write(sirnou)
except:
    print("Parola e gresita")
