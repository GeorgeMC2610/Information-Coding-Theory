for i in range(10):
    print(i)


G=Matrix(GF(2),[[1 , 0 , 0 , 0 , 1 , 0],
         [0 , 1 , 0 , 0 , 1 , 1],
         [0 , 0 , 1 , 0 , 1 , 1],
         [0 , 0 , 0 , 1 , 1 , 0]]
)
c=vector(GF(2),[1,1,1,0])
c*G


for i in range(16):
    tmp=bin(i)[2:]
    tmp=(3*"0"+tmp)[-4:]
    tmp=list(tmp)
    tmp=[int(j)  for j in tmp]
    c=vector(GF(2),tmp)
    print(c*G)

H=Matrix(GF(2),[[1,1,1,0,0,0],[0,0,0,1,1,1]]
)

H*(vector([1, 1, 1, 1, 0, 0])+vector([0, 0, 0, 1, 0, 0]))

H*(vector([0, 0, 1, 0, 1, 1])+vector([0, 1, 0, 0, 0, 0]))
