first=[1,2,3,4,5]
print(first)

second= first
second.append(6)
print(second)
print(first)

third=second.copy()
third.append(7)
print(third)
print(second)
