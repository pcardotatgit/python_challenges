# Challenge

Create a python script which Retrieves the list here :

https://raw[.]githubusercontent[.]com/tg12/pihole-phishtank-list/master/list/phish_domains[.]txt

Extract from this list only domain names which ends with : **.co** 

Create a resulting json file ( web.json ) file which contains a key named **domains** which contain a list of all extracted domains that end with  : .co

And which contains another key named **nb_of_domains** that contains the number of extracted domains

exemple :

{

    "domains": [

        "0010101.linkn1.repl.co",

        ....

        ....

        ....

    ],

    "nb_of_domains": 611
    
}


Allocated time : 30 minutes
