# coding: utf-8
fa = open("resultat.txt", "w")

# loop through .txt file and append every domain to list, skip comments
domainList = []
with open('domains.txt') as inputfile:
	for line in inputfile:
		if line[0] == "#" or line.strip() == "Site":
			pass
		else:
			domainList.append(line.strip())

# time for AlertTime and EventTime when domains are added to Umbrella
#time = datetime.now().isoformat()

# loop through all domains
nb=0
for domain in domainList:
	if domain.endswith(".com"):
		#print(domain)
		fa.write(domain)
		fa.write("\r\n")
		nb+=1
print ('Nb =',str(nb))		
fa.close()