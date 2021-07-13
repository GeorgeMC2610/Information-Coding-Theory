import random

diastasi = int(input("Εισάγετε πόσα ψηφία είναι το μήνυμα: "))

pinakes = []
random_addition = random.randint(1, diastasi - 1)
for i in range(diastasi):
    tmplist = [0 for j in range(diastasi)]
    tmplist[i] = 1
    pinakes.append(tmplist)
    for j in range(random_addition):
        tmplist.append(random.randint(0, 2))

G1 = Matrix(GF(2), pinakes)
print(G1)

pinakes = []
for i in range(diastasi):
    tmplist = [random.randint(0, 2) for j in range(diastasi)]
    pinakes.append(tmplist)

S = Matrix(GF(2), pinakes)

print(S)

pinakes = []
for i in range(G1.ncols()):
    tmplist = [random.randint(0, 2) for j in range(diastasi_coded)]
    pinakes.append(tmplist)

P = Matrix(GF(2), pinakes)
print(P)
