variable = "apple, orange, strawberry-data"

word_list=variable.split(',')

print(word_list)

for word in word_list[:]
    word=("*"+word.replace(" ","")+"*").upper()
    word=word.replace("-DATA","")
    print(word)

