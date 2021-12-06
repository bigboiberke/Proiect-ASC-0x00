f = open("input.txt", 'r')
g = open("output", 'rb')
h = open("parola.txt", 'w')
textus = f.read()
bitus = g.read()
bitus = bitus.decode("utf-8")
lungime = len(bitus)
aha = ""
for i in range(lungime):
    aha = aha + chr(ord(textus[i])^ord(bitus[i]))
h.write(aha)