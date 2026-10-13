word = input().lower()
result = "".join("." + c for c in word if c not in "aoyeui")
print(result)