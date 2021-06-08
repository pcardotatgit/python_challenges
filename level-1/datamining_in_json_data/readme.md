# Challenge

Have a look to the follwoing API :

	http://restcountries.eu/rest/v2/all?fields=name;population;region;capital;flag;borders;alpha3Code
	
It gives you the details of all countries on earth.


Create some scripts that get this content from the INTERNET, and which  gives you the answers to the following questions :

- **challenge 1** : How many coutries have a common border with France ?
- **challenge 2** : How many countries have a common border together and with FRANCE ?
- **challenge 3** : How many countries don't have any borders with other countries ?
- **challenge 4** : Create an html file that output in your browser all country flags for the first 10 countries.

- **challenge 5** : Display a list which contains most populated countries with their population in desc order . Format the list the following way

```
[
{ "contry_name_1": population_1},
{ "contry_name_2": population_2},
....
{ "contry_name_n": population_n}
]
```

- **challenge 6** : display a list of the most populated regions in the desc order. Format the list this way 

```
[
{ "region_name_1": population_1},
{ "region_name_2": population_2},
....
{ "region_name_n": population_n}
]
```

- **challenge 7** :  Display a text relation graph that start with a choosen country which will be the root. and in this graph link all countries that have a border with the parent countries. Create a tree and don't loop on countries that already are in your tree.

Allocated Time :  Let's say one day if you start from 0. 