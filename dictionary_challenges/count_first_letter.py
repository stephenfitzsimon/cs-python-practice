# Write your count_first_letter function here:
def count_first_letter(names):
    letters = dict()
    for k in names.keys():
        if k[0] not in letters.keys():
            letters[k[0]] = 0
        letters[k[0]] += len(names[k])
    return letters


# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}