def main():

    a = [[0, 0],[0, 0]]
    b = [[0, 0],[0, 0]]

    n = len(a) # nombre de lignes de A
    m = len(b[0]) # nombre de colonnes de B
    p = len(b) # nombre de lignes de B 

    for i in range(2):
        for k in range(len(a[i])):
            a[i][k] = int(input("Valeur de la matrice A ? \n"))
    for i in range(2):
        for k in range(len(b[i])):
            b[i][k] = int(input("Valeur de la matrice B  ? \n"))

    c = [[0]*m for i in range(n)] # matrice de n lignes et m colonnes
    # parcourir les lignes de A
    for i in range(n):
        # parcourir les colonnes de B
        for j in range(m):
            # parcourir les lignes de B
            for k in range(p):
                c[i][j] += a[i][k] * b[k][j]

    print("matrice A : ", a)
    print("matrice B : ", b)
    print("matrice A * matrice B : ", c)

if __name__ == "__main__":
 main()