# Write your max_key function here:
def max_key(my_dictionary):
    max_key = None
    max_value = 0
    for k in my_dictionary.keys():
        if max_value < my_dictionary[k]:
            max_key = k
            max_value = my_dictionary[k]
    return max_key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"