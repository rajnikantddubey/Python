#Create a list of names and print the second item.
lis = ['raj','john','james','josh','jake']
print(lis[1])

# 2. Create a list of sports and then replace the second item with another sport.
lis2=['cricket','football','basketball','tennis','baseball']
lis2[1]='volleyball'
print(lis2)

# 3. Create a list containing numbers and delete the fifth number from the array.
lis3=[1,2,3,4,5]
del lis3[4]
print(lis3)


# 4. Create two lists of numbers and merge them. 
lis4 = [1,2,3,4,5]
lis5=[6,7,8,9,10]
print(lis4+lis5)

# 5. Create a list of numbers and find the length, minimum, and maximum.
lis6=[1,2,3,4,5,6,7,8,9,10]
print(len(lis6))
print(max(lis6))
print(min(lis6))

# 6. Create a dictionary of students and scores and print out a student’s score.
dict1={'raj':90,'john':85,'james':95,'josh':100,'jake':80}
print(dict1['raj'])

# 7. Create a dictionary with the key being names and values being ages and then delete the second key/value pair.
dict2={'raj':20,'john':25,'james':30,'josh':35,'jake':40}
del dict2['john']
print(dict2)

# 8. Create a dictionary of names and ages and then print out all the keys and values
data = {"Rachel": 17, "Rahul": 61, "Anna": 15}
print(data.keys)
print(data.values)

# 9. Create a tuple of your favorite movies 
tup=('The Godfather','The Dark Knight','The Matrix','The Shawshank Redemption')
print(tup)
# 10. Create a tuple and print all the items from the first to third index.
tup2=('The Godfather','The Dark Knight','The Matrix','The Shawshank Re')
print(tup2[0:3])      
