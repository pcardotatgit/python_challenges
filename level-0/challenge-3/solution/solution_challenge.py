# coding: utf-8
# 
import requests
fa = open("resultat.txt", "w")
# recuperer la liste contenu derriere l' URL et la stocker dans un fichier texte
result = requests.get("http://www.jamessawyer[.]co[.]uk/MASTER[.]txt")
list = result.text.splitlines()
count = 0
for ligne in list:
	#if domain.find(".info") >= 0:
	if ligne.endswith(".info"):
		fa.write(ligne)
		fa.write("\r\n")
		count +=1
print (" result = " + str(count))
fa.close()