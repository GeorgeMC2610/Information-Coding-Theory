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