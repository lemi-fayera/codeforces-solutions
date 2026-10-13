word = input()

upper = sum(1 for char in word if char.isupper())
lower = sum(1 for char in word if char.islower())

if lower >= upper:
    print(word.lower())
else:
    print(word.upper())