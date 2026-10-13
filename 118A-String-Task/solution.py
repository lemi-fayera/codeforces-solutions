word = input()

letters = word.lower()
result = []
for letter in letters:
    if letter in "aeiouy":
        continue
    result.append(".")
    result.append(letter)
last = "".join(result)

print(last)
    