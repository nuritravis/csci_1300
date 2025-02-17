######################################
# hw08 Question 1 template
######################################
######################################
# some sample data; of course your program should work on any such data
collection = [25, 100, 35, 14, 28, 44, 100, 28, 35, 35, 26]
value = 35
######################################
######################################

myCount = 0
for i in range(0, len(collection)):
    if collection[i] == value:
        myCount += 1


######################################
######################################
# Let's see your results
print(myCount)
######################################
