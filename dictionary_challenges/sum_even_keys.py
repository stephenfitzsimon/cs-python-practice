# Write your sum_even_keys function here:
def sum_even_keys(my_dictonary):
    return sum([my_dictonary[k] for k in my_dictonary.keys() if not k%2 ])

# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6