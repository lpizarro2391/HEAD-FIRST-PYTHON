phrase="don't panic!"
plist= list(phrase)
print(phrase)
print(plist)
<<<<<<< HEAD

for i in range(4):
    plist.pop()
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(),plist.pop()])
plist.insert(2,plist.pop(3))

new_phrase=''.join(plist)
print(plist)
=======
print(plist[1:3])
new_phrase=''.join(plist[1:3])
new_phrase= ''.join(plist[1:3])+''.join(plist[5])+''.join(plist[4])+''.join(plist[7])+''.join(plist[6])
>>>>>>> 75a1dbe7d518ab783e33a0937d9f671698936df3
print(new_phrase)
