import random
import math

diastasi_coded_kyklikou = 12 #input

x = PolynomialRing(RationalField(), 'x').gen()
f = x^(diastasi_coded_kyklikou) + 1
print("f(x) Starting Polynomial:")
print(f)
print()

factored_f = f.factor()[0][0]

if factored_f.degree() == f.degree() and f.degree() % 2 == 0:
    factored_f = x^2 + 1 + 2*x * round(math.cos(math.pi/(f.degree()/2)), 3)
elif factored_f.degree() == f.degree() and f.degree() % 2 != 0:
    factored_f = (x + 1) * (x^2 + 1 + 2*x * math.cos(2*math.pi/(f.degree())))

print("First term of factored f(x): ")
print(factored_f)
print()

print("The dimensions of the linear code has to be: ")
diastasi_coded          = diastasi_coded_kyklikou - factored_f.degree()
print(str(diastasi_coded_kyklikou) + " - " + str(factored_f.degree()) + " = " + str(diastasi_coded))
print()

diastasi_kyklikou       = diastasi_coded
msg                     = [0, 1, 0, 1, 1] #input, has to be until diastasi_coded-1
diastasi                = len(msg)

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
print("Linear Coded Message: ")
print(c)
print()

pinakes = []
print("All linear coded messages for " + str(diastasi) + "-bit inputs: ")
for i in range(2**diastasi):
    tmp=bin(i)[2:]
    tmp=((diastasi-1)*"0"+tmp)[-diastasi:]
    tmp=list(tmp)
    tmp=[int(j) for j in tmp]
    pinakes.append(tmp)
c = Matrix(GF(2), pinakes)
print(c*Gtonos)
print()

pinakes = []
tmp = factored_f.coefficients(sparse=False) + [0 for i in range(diastasi_kyklikou - 1)]
pinakes.append(tmp)
for i in range(diastasi_kyklikou - 1):
    tmp = [tmp[-1]] + tmp[:-1]
    pinakes.append(tmp)

G2 = Matrix(GF(2), pinakes)

print("Coefficients of factored f(x): ")
print(G2[0])
print()

print("G2: ")
print(G2)
print()