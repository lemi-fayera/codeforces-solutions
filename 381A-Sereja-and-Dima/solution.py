n = int(input())
cards = list(map(int, input().split()))

seraja = dima = 0
left, right = 0, n - 1
turn = True

while left <= right:
    card = cards[left] if cards[left] > cards[right] else cards[right]

    if cards[left] > cards[right]:
        left += 1
    else:
        right -= 1

    if turn:
        seraja += card
    else:
        dima += card

    turn = not turn

print(seraja, dima)