print("M Rakesh")
print("192421006")

r1 = int(input("Enter number of rows in Matrix A: "))
c1 = int(input("Enter number of columns in Matrix A: "))

A = []
print("Enter Matrix A:")
for i in range(r1):
    row = list(map(int, input().split()))
    A.append(row)

r2 = int(input("Enter number of rows in Matrix B: "))
c2 = int(input("Enter number of columns in Matrix B: "))

B = []
print("Enter Matrix B:")
for i in range(r2):
    row = list(map(int, input().split()))
    B.append(row)

if c1 != r2:
    print("Matrix multiplication is not possible.")
else:
    result = [[0 for j in range(c2)] for i in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += A[i][k] * B[k][j]

    print("Resultant Matrix:")
    for row in result:
        print(row)
