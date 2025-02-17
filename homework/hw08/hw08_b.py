
######################################
# hw08 Question 2 template
######################################
######################################
# some sample data; of course your program should work on any such data
words = ['apple', 'kayak', 'aha', 'midnight', 'noon']
######################################
######################################

palindromes = []
for i in range(0, len(words)):
    if len(words[i]) >= 5:
        if words[i] == words[i][::-1]:
            palindromes.append(words[i])

######################################
######################################
# Let's see your results
print(palindromes)
######################################
