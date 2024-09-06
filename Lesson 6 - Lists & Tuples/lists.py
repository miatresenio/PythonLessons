users = ['Mia', 'Myca', 'Nau']

data = ['Mia', 20, True]

emptylist = []
    
print("Mia" in emptylist)

print(users[0])
print(users[-2])

print(users.index('Nau'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Taylor')
print(users)

users += ['Swift']
print(users)

users.extend(['Deib', 'Lohr'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob')
print((users))

users[2:2] = ['Aubrey', 'Pau']
print(users)

users[1:3] = ['Sam','Liyan']
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

data.clear()
print(data)

users[1:2] = ['mia']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4,42,78,1,5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))       # global sorted function
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([2, "fries", True])
print(mylist)




# Tuples - cannot be change

mytuple = tuple(('Mia', 20, True))

anothertuple = (1,4,2,8,2,2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))