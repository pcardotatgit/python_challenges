# -*- coding: UTF-8 -*-

from struct import pack

image=input("Enter the BMP image name with it's extension .bmp : ")
#print("l image modifiee sera dans le fichier image2.bmp")
fich=open(image,"rb")
fichbis=open("image.txt","w")
 
fich.seek(10)
#on lit les 4 octets correspondants � l'offset qui sont situ�s apr�s le 10�me octet
m=fich.read(4)
 
def num(m):
    """retourne le nombre correspondant a 4 octets lus en little indian"""
 
    return m[0]+m[1]*16*16+m[2]*16**4+m[3]*16**6
offset=num(m) #cela donne le d�calage entre le d�but du fichier et le d�but de l'image
print("l offset est ( localisation du premier pixel apres l entete ) : ",offset) #pour v�rification
#on se remet au d�but du fichier
fich.seek(0)
#on lit l'ent�te et on la recopie dans le nouveau fichier
deb=fich.read(offset)
#on cherche la largeur et la hauteur dans l'ent�te
#largeur 4 octets en commen�ant par�s le 18�me
fich.seek(18)
m=fich.read(4)
 
largeur=num(m)
print("Image's width is : "  + str(largeur) + " pixels ")
 
#la hauteur les 4 octets suivants
m=fich.read(4)
hauteur=num(m)
print("Image's heigth is : " +str(hauteur) + " lignes" )
#on se place au d�but de l'image
fich.seek(offset)
 
#on lit les diff�rentes lignes
nombre=0
for j in range(hauteur):
    for i in range(largeur):
        #on lit 3 octets pour les trois couleurs
        m=fich.read(3)
        #on fait des modifications sur chaque couleur(ici juste pour essai)
        #on pourra ensuite faire d'autres modifications...
        #attention de rester entre 0 et 255 !
        if len(m)>0 and len(m)==3:
            l=str(m[0])+';'+str(m[1])+';'+str(m[2])
            fichbis.write(l)
            fichbis.write('\r')			
            if m[0]==255 and m[1]==255 and m[2]==255:
                nombre+=1
				 
fich.close()
fichbis.close()
print ('The number of white pixel is equal to :'+ str(nombre))