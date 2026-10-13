n = int(input())

solved = 0

for _ in range(n):
    answers = list(map(int, input().split()))

    if sum(answers) >= 2:
        solved += 1

print(solved)
