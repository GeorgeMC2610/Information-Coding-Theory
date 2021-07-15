import random
import math

diastasi_coded_kyklikou = 7 #input >=3 kai peritto

F.<x> = GF(2)[]
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
msg                     = [1,0,1] #max length is diastasi_coded - 1
diastasi                = len(msg)

print("input code is:")
print(Matrix(GF(2),msg))
print()

msg = Matrix(GF(2), msg)

#Creation of a random inversable S matrix. S must have diastasi X diastasi dimensions.
#S is inversable because it becomes from an I_{diastasi} matrix on which only a few row
#transformations have been made(we add random rows together)
S = matrix.identity(diastasi)
S = Matrix(GF(2), S)
for i in range(2*diastasi):
    random_row1 = random.randint(0, diastasi -1)
    random_row2 = random.randint(0, diastasi -1)
    S[random_row1] = S[random_row1] + S[random_row2]

print("MATRIX S: ")
print(S)
print()

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

#make a random permutation of I and name it P
perm_el = [i for i in range(1,diastasi_coded+1)] #(1,2,3,4,...,diastasi_coded)
random.shuffle(perm_el)
perm_el = str(tuple(perm_el))

perm1 = [i for i in range(1,(diastasi_coded)//2 + 1)] #half of the above shuffled
random.shuffle(perm1)
perm1 = tuple(perm1)

perm2 = [i for i in range((diastasi_coded)//2 + 1, diastasi_coded+1)] #other half of the above shuffled
random.shuffle(perm2)
perm2 = tuple(perm2)

if(len(perm1) == 1 and len(perm2) == 1):
    P=Matrix([[0,1],[1,0]])

elif(len(perm1) == 1 and len(perm2) != 1):
    perm1 = str(perm1).replace(',', '')
    perm2 = str(perm2)

    P = matrix.identity(diastasi_coded)
    Per = PermutationGroup([perm1 + perm2, perm_el]) #ex. (1,3,2)(5,4),(1,2,3,4,5) means that the first column will be the third column,
    sigma, tau = Per.gens()                          #the third column will be the second one, the second one will be the first one, the
    P.permute_columns(sigma)                         #fifth one will be the forth one and the forth one will be the fifth one

elif(len(perm1) != 1 and len(perm2) == 1):
    perm2 = str(perm2).replace(',', '')
    perm1 = str(perm1)

    P = matrix.identity(diastasi_coded)
    Per = PermutationGroup([perm1 + perm2, perm_el])
    sigma, tau = Per.gens()
    P.permute_columns(sigma)

else:
    perm1 = str(perm1)
    perm2 = str(perm2)

    P = matrix.identity(diastasi_coded)
    Per = PermutationGroup([perm1 + perm2, perm_el])
    sigma, tau = Per.gens()
    P.permute_columns(sigma)

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
for i in range(2**diastasi):
    tmp=bin(i)[2:]
    tmp=((diastasi-1)*"0"+tmp)[-diastasi:]
    tmp=list(tmp)
    tmp=[int(j) for j in tmp]
    pinakes.append(tmp)

#multipling the above matrix with Gtonos we get all the corresponding encoded messages for linear code
C1 = Matrix(GF(2), pinakes)
print("All linear encoded messages for " + str(diastasi) + "-bit inputs: ")
print(C1*Gtonos)
print()

cyclic=codes.CyclicCode(generator_pol = factored_f_term1, length = diastasi_coded_kyklikou)
G2 = cyclic.generator_matrix()

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

minimum_distance = cyclic.minimum_distance()

print("All cyclic encoded messages for " + str(diastasi_kyklikou) + "-bit inputs:")
print(C2)
print()

print("minimum distance of cyclic code:")
print(minimum_distance)
print()

#making a matrix with a count of aces between 1 and minimum_distance - 1
assoi = [1 for i in range(random.randint(1, minimum_distance - 1))]

#add zeros to the above matrix, until we get a 1 X diastasi_coded_kyklikou dimensional error vector
sfalma = assoi + [0 for i in range(diastasi_coded_kyklikou - len(assoi))]

#shuffle sfalma vector in order to get a random error vector
random.shuffle(sfalma)
sfalma = vector(GF(2), sfalma)
print("Noise")
print(sfalma)
print()

ctonos = cyclic.encode(c[0])
print("C' message:")
print(ctonos)
print()

corrupted_ctonos = ctonos + sfalma
print("Corrupted Message:")
print(corrupted_ctonos)
print()

decoded = cyclic.decode_to_message(vector(GF(2), corrupted_ctonos))
print("Decoded corrupted message:")
print(decoded)









