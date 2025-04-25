risada = input()
vogais = [c for c in risada if c in 'aeiou']

if vogais == vogais[::-1]:
    print("S")
else:
    print("N")