vowels=['a','e','i','o','u']
word=input("Provide a word to searh for vowels: ")
found=[]
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)


for vowel in found:
    print(vowel)

    found={}
    for k in sorted (found):
        print(k,'was found', found[k],'time(s).')
