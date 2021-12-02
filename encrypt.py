cheie = input("Parola criptare: ")
f = open(input("Nume fisier pentru criptare: "))
g = open(input("Nume fisier criptat: "), "wb")
sir = f.read()
sirnou = ""
j = 0
lungimecheie = len(cheie)
lungimesir = len(sir)
for i in range(lungimesir):
    if j == lungimecheie:
        j = 0
    sirnou = sirnou + chr(ord(sir[i]) ^ ord(cheie[j]))
    j = j+1
sirnou = sirnou.encode("utf-8")
g.write(sirnou)
