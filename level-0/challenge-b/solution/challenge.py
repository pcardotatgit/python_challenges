from crayons import blue, green, white, red, yellow,magenta, cyan

WordList = ['green','red','cyan']

#go=1

while go:
    word=input('Enter green or red or cyan : ')      
    word_out=word.upper()
    output=f'Ok {word} is {word_out}'
    word=word.lower()   
    if word in WordList:   
        if word=='green':            
            print(green(output)) 
        if word=='red':            
            print(red(output))  
        if word=='cyan':            
            print(cyan(output))            
    else:
        print(white("not good"))
        go=0        