strings = [i for i in input("Enter strings : ").split()]

allletters = list(map(lambda string: string.upper(), filter(lambda string: string.isalpha(), strings)))
alldigits = list(map(lambda num: int(num) * int(num), filter(lambda string: string.isdigit(), strings)))
allalnum = list(filter(lambda string: string.isalnum(), strings))

print(f"All Letters: {allletters}")
print(f"All Digits: {alldigits}")
print(f"All Alphanumeric: {allalnum}")