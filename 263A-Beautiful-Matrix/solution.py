matrix=[]
for _ in range(5):
    temp = list(map(int, input().split()))
    matrix.append(temp)



for row in range(5):
    for col in range(5):
        if matrix [row][col] == 1:
            i,j = row, col
print((abs(2-i)+ abs(2-j)))