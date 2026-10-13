n = int(input())
values = list(map(int, input().split()))

sorted_values = sorted(values, reverse=True)
total = sum(values)
count = 0
sum = 0

for value in sorted_values:
    count += 1
    sum += value
    if sum > (total - sum):
        break

print(count)