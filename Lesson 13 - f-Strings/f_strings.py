# fruits = "blueberries"
# nof = 5
# name = "Mia"

# print(name + " have " + str(nof) + " " + fruits + ".")

person = "Mia"
coins = 3

print("\n" + person + " has " + str(coins) + "coins left.")  # Concatinating with the + symbol

message = "\n%s has %s coins left." %(person, coins)   # % method
print(message)

message = "\n{} has {} coins left.".format(person, coins)   # Another way of achieving format of the string using FORMAT METHOD
print(message)

message = "\n{1} has {0} coins left.".format(coins, person)   # Format method (put index method)
print(message)

message = "\n{person} has {coins} coins left.".format(coins=coins, person=person)   #
print(message)


player = { 'person': 'Mia', 'coins': 3 }


message = "\n{person} has {coins} coins left.".format(**player)   # Dictionary 
print(message)


############################
# f-Strings! This is the way.

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2 * 5} coins left."
print(message)

message = f"\n{person.lower()} has {2 * 5} coins left."
print(message)

message = f"\n{player['person']} has {2 * 5} coins left."
print(message)


#################################
# You can pass formatting options

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")


# Can put this in a loop
for num in range(1,11):
    print(f"\n2.25 times {num} is {2.25 * num:.2f}")
    
for num in range(1,11):
    print(f"{num} divided by 2.52 is {num / 4.52:.2%}")
