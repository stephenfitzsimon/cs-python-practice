# Write your make_spoonerism function here:
def make_spoonerism(word1, word2):
    first = word2[0] + word1[1:]
    second = word1[0] + word2[1:]
    return first + " " + second

# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a