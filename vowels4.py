<<<<<<< HEAD
vowels=['a','e','i','o','u']
word=input("Provide a word to searh for vowels: ")

found={}


found ['a']=0
found ['e']=0
found ['i']=0
found ['o']=0
found ['u']=0

for letter in word:
    if letter in vowels:
       found[letter]+=1

for k,v in sorted(found.items()):
    print(k,'was found',v,'time(s).')
=======
vowels = ['a', 'e', 'i', 'o', 'u']
word= input("Indique la palabra que quiere revisar")

found={}

found['a']=0
found['e']=0
found['i']=0
found['o']=0
found['u']=0

for letter in word:
    if letter in vowels:
        found[letter] += 1
for k,v in sorted(found.items()):
    print(k, 'was found', v, 'times(s).')
>>>>>>> 75a1dbe7d518ab783e33a0937d9f671698936df3
