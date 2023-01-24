# Write your add_ten function here:
def add_ten(my_dictionary):
    return {k:v+10 for (k, v) in zip(my_dictionary.keys(), my_dictionary.values())}

# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}