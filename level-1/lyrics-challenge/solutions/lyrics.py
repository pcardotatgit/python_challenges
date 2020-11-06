from PyLyrics import *
name = str(raw_input("Enter a song: "))
writer= str(raw_input("Enter the writer:"))
print(PyLyrics.getLyrics(writer,name)) #Print the lyrics directly