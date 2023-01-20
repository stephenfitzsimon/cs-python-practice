# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
    idx_one = word.find(start)
    idx_two = word.find(end)
    if idx_one == -1 or idx_two == -1:
        return word
    else:
        return word[idx_one+1:idx_two]

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"