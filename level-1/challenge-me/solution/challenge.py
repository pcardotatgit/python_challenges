TROUBLESHOOT THIS SCRIPT !  IT DOESN'T WORK AS IS !!!
word = 'ObservATlo'
#convert the word into a list
wordlist=[]
for letter in word:
wordlist.append(letter)
#reverse order this wordlist    
wordlist.sort(reverse=True)    
print(wordlist)
#create the dictionary
dico={}
i=0
new_word=''
for letter in wordlist:
#print("The ASCII value of '" + letter + "' is", ord(letter))
dico.update({letter : i+ord(letter)})
i+=1
new_word+=chr(i+ord(letter))
print('The new word is : ',new_word)