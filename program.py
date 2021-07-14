import random
import math

diastasi_coded_kyklikou = 16 #input >=3

x = PolynomialRing(RationalField(), 'x').gen()
f = x^(diastasi_coded_kyklikou) + 1
print("Starting cyclic code polynomial:")
print(f)
print()

#trying to factor polynomial
print("Trying to factor x^"+str(diastasi_coded_kyklikou)+" + 1:")
print(f.factor())
print()

#-If factorisation was successfull, get a random term
#-If factorisation was not successfull, we factor the polynomial
#depending on the product formulas that can be found in:
#note that we take only the first term for k=0(even case) or k=1(odd case)

terms = len(factor(f))
if f.factor()[0][0].degree() != f.degree():
    rand_term = random.randint(0,terms - 1)
    factored_f_term1 = f.factor()[rand_term][0]
    if(diastasi_coded_kyklikou - factored_f_term1.degree() == 1): #if we get a term that requires cyclic code input = 1, take first term
        factored_f_term1 = f.factor()[0][0]

#if polynomial has even degree
elif f.factor()[0][0].degree() == f.degree() and f.degree() % 2 == 0:
    print("Factor failed, so we take the first term of the formula")
    print()
    factored_f_term1 = x^2 + 1 + 2*x * round(math.cos(math.pi/(f.degree()/2)))
#if polynomial has odd degree
elif f.factor()[0][0].degree() == f.degree() and f.degree() % 2 != 0:
    print("Factor failed, so we take the first term of the formula")
    print()
    factored_f_term1 = (x + 1) * (x^2 + 1 + 2*x * round(math.cos(2*math.pi/(f.degree()))))

print("Selected term of factored polynomial(this is our generator polynomial g(x)): ")
print(factored_f_term1)
print()

print("The dimensions of the linear code has to be: ")
diastasi_coded          = diastasi_coded_kyklikou - factored_f_term1.degree()
print(str(diastasi_coded_kyklikou) + " - " + str(factored_f_term1.degree()) + " = " + str(diastasi_coded))
print()

diastasi_kyklikou       = diastasi_coded
msg                     = [1,0,1,0] #max length is diastasi_coded - 1
diastasi                = len(msg)

msg = Matrix(GF(2), msg)

#creation of G1 matrix. G1 must have diastasi X diastasi_coded dimensions (P part on G1 matrix is added randomly)
pinakes = []
addition = diastasi_coded - diastasi
for i in range(diastasi):
    tmplist = [0 for j in range(diastasi)]
    tmplist[i] = 1
    pinakes.append(tmplist)
    for j in range(addition):
        tmplist.append(random.randint(0, 1))

G1 = Matrix(GF(2), pinakes)
print("MATRIX G1: ")
print(G1)
print()

#creation of random S matrix. S must have diastasi X diastasi dimensions
pinakes = []
for i in range(diastasi):
    tmplist = [random.randint(0, 1) for j in range(diastasi)]
    pinakes.append(tmplist)

S = Matrix(GF(2), pinakes)
print("MATRIX S: ")
print(S)
print()

#creation of random P matrix. P must have diastasi_coded X diastasi_coded dimensions
pinakes = []
for i in range(diastasi_coded):
    tmplist = [random.randint(0, 1) for j in range(diastasi_coded)]
    pinakes.append(tmplist)

P = Matrix(GF(2), pinakes)
print("MATRIX P: ")
print(P)
print()

#creation of final Generator matrix G'. G' has diastasi X diastasi_coded dimensions
Gtonos = S * G1 * P
print("G' = S * G1 * P: ")
print(Gtonos)
print()

#encoded message with linear code
c = msg * Gtonos
print("Linear Encoded Message: ")
print(c)
print()

#creating a matrix with all the diastasi-bit possible inputs as rows
pinakes = []
print("All linear encoded messages for " + str(diastasi) + "-bit inputs: ")
for i in range(2**diastasi):
    tmp=bin(i)[2:]
    tmp=((diastasi-1)*"0"+tmp)[-diastasi:]
    tmp=list(tmp)
    tmp=[int(j) for j in tmp]
    pinakes.append(tmp)

#multipling the above matrix with Gtonos we get all the corresponding encoded messages for linear code
C1 = Matrix(GF(2), pinakes)
print(C1*Gtonos)
print()

#get the coefficients of g(x) and make the generator matrix G2 (negative coefficients mod 2 are positive, so -1 will be 1)
pinakes = []
tmp = factored_f_term1.coefficients(sparse=False)[::-1] + [0 for i in range(diastasi_kyklikou - 1)]
pinakes.append(tmp)
for i in range(diastasi_kyklikou - 1):
    tmp = [tmp[-1]] + tmp[:-1]
    pinakes.append(tmp)

G2 = Matrix(GF(2), pinakes)

print("Coefficients of factored g(x) (mod2): ")
print(G2[0])
print()

print("G2: ")
print(G2)
print()

#creating a matrix with all the diastasi_kyklikou-bit possible inputs as rows
pinakes = []
for i in range(2**diastasi_kyklikou):
    tmp=bin(i)[2:]
    tmp=((diastasi_kyklikou-1)*"0"+tmp)[-diastasi_kyklikou:]
    tmp=list(tmp)
    tmp=[int(j) for j in tmp]
    pinakes.append(tmp)

#multipling the above matrix with G2 we get all the corresponding encoded messages for cyclic code
C2 = Matrix(GF(2), pinakes)
C2 = C2 * G2

#count all the aces on each encoded message of C2, and get the minimum C2 distance
count_of_aces = []
for i in C2:
    count_of_aces.append(len([j for j in i if j == 1]) if len([j for j in i if j == 1]) != 0 else 10000000)


minimum_distance = min(count_of_aces)

print("All cyclic encoded messages for " + str(diastasi_kyklikou) + "-bit inputs:")
print(C2)

#making a matrix with a count of aces between 1 and minimum_distance - 1
assoi = [1 for i in range(random.randint(1, minimum_distance - 1))]

#add zeros to the above matrix, until we get a 1 X diastasi_coded_kyklikou dimensional error vector
sfalma = assoi + [0 for i in range(diastasi_coded_kyklikou - len(assoi))]

#shuffle sfalma vector in order to get a random error vector
random.shuffle(sfalma)
sfalma = Matrix(GF(2), sfalma)
print("Noise")
print(sfalma)
print()

ctonos = c * G2
print("C' message:")
print(ctonos)
print()

corrupted_ctonos = ctonos + sfalma
print("Corrupted Message:")
print(corrupted_ctonos)








