s = input().strip()
n = len(s)

prefix = [0] * (n + 1)

for i in range(1, n):
    prefix[i + 1] = prefix[i] + (s[i] == s[i - 1])

m = int(input())

for _ in range(m):
    l, r = map(int, input().split())
    print(prefix[r] - prefix[l])