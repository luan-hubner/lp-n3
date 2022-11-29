import random
import numpy as np

cards = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4', 'C1', 'C2', 'C3', 'C4', 'D1', 'D2', 'D3', 'D4', 'E1', 'E2', 'E3', 'E4', 'F1'];
random.shuffle(cards)

A = cards[0:7]
B = cards[7:14]
C = cards[14:21]

tablement1 = "{} {} {}\n{} {} {}\n{} {} {}\n{} {} {}\n{} {} {}\n{} {} {}\n{} {} {}".format(A[0], B[0], C[0], A[1], B[1], C[1], A[2], B[2], C[2], A[3], B[3], C[3], A[4], B[4], C[4], A[5], B[5], C[5],A[6], B[6], C[6]);
print(tablement1);

firstChoose = input("Escolha uma carta, memorize e digite qual coluna ela está: (A, B ou C)");

E1 = [];

if (firstChoose == "A"):
    E1 = [*B, *A, *C];
elif (firstChoose == "B"):
    E1 = [*A, *B, *C];
else:
    E1 = [*A, *C, *B];

D = [E1[0], E1[3], E1[6], E1[9], E1[12], E1[15], E1[18]]
E = [E1[1], E1[4], E1[7], E1[10], E1[13], E1[16], E1[19]]
F = [E1[2], E1[5], E1[8], E1[11], E1[14], E1[17], E1[20]]

tablement2 = "{} {} {}\n{} {} {}\n{} {} {}\n{} {} {}\n{} {} {}\n{} {} {}\n{} {} {}".format(D[0], E[0], F[0], D[1], E[1], F[1], D[2], E[2], F[2], D[3], E[3], F[3], D[4], E[4], F[4], D[5], E[5], F[5], D[6], E[6], F[6]);
print(tablement2);

secondChoose = input("Escolha a coluna que a sua carta está: (A, B ou C)");

E2 = [];

if (secondChoose == "A"):
    E2 = [*E, *D, *F];
elif (secondChoose == "B"):
    E2 = [*D, *E, *F];
else:
    E2 = [*D, *F, *E];

G = [E2[0], E2[3], E2[6], E2[9], E2[12], E2[15], E2[18]]
H = [E2[1], E2[4], E2[7], E2[10], E2[13], E2[16], E2[19]]
I = [E2[2], E2[5], E2[8], E2[11], E2[14], E2[17], E2[20]]


tablement3 = "{} {} {}\n{} {} {}\n{} {} {}\n{} {} {}\n{} {} {}\n{} {} {}\n{} {} {}".format(G[0], H[0], I[0], G[1], H[1], I[1], G[2], H[2], I[2], G[3], H[3], I[3], G[4], H[4], I[4], G[5], H[5], I[5], G[6], H[6], I[6]);
print(tablement3);

thirdChoose = input("Escolha a coluna que a sua carta está: (A, B ou C)");

E3 = [];

if (thirdChoose == "A"):
    E3 = [*H, *G, *I];
elif (thirdChoose == "B"):
    E3 = [*G, *H, *I];
else:
    E3 = [*G, *I, *H];

print("A sua carta escolhida foi: ", E3[10])