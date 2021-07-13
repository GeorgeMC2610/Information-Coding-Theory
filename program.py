import random

msg = [0, 1, 0, 1, 1]
diastasi = len(msg)
diastasi_coded = 8

msg = Matrix(GF(2), msg)

pinakes = []
random_addition = random.randint(1, diastasi - 1)
for i in range(diastasi):
    tmplist = [0 for j in range(diastasi)]
    tmplist[i] = 1
    pinakes.append(tmplist)
    for j in range(random_addition):
        tmplist.append(random.randint(0, 2))

G1 = Matrix(GF(2), pinakes)
print("MATRIX G1: ")
print(G1)
print()

pinakes = []
for i in range(diastasi):
    tmplist = [random.randint(0, 2) for j in range(diastasi)]
    pinakes.append(tmplist)

S = Matrix(GF(2), pinakes)
print("MATRIX S: ")
print(S)
print()

pinakes = []
for i in range(G1.ncols()):
    tmplist = [random.randint(0, 2) for j in range(diastasi_coded)]
    pinakes.append(tmplist)

P = Matrix(GF(2), pinakes)
print("MATRIX P: ")
print(P)
print()

Gtonos = S * G1 * P
print("G': ")
print(Gtonos)
print()

c = msg * Gtonos
print("Coded Message: ")
print(c)
print()