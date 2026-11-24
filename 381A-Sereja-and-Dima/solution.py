n = int(input())
cards = list(map(int, input().split()))

seraja = 0
dima = 0
ser = True
left = 0
right = len(cards)-1

while left <= right:
    if cards[left] > cards[right]:
        if ser:
            seraja += cards[left]
            ser = False
            left += 1
        else:
            dima += cards[left]
            ser = True
            left += 1
    else:
        if ser:
            seraja += cards[right]
            ser = False
            right -= 1
        else:
            dima += cards[right]
            ser = True
            right -= 1
print(seraja, dima)