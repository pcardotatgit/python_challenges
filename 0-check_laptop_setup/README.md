# Introduction

The following instructions aim to help you to check that you have installed into your laptop the minimum tools required for Python labs.

# Instructions:

- Create a working directory, into your Devolpement Laptop
- Open a console window and change directory to your working directory

Based on the instruction given by the DEVNET documentation, create a python virtual environment and activate it

## Installation

Installing these scripts is pretty straight forward . You can just copy / and paste them into you python environment but a good practice is to run them into a python virtual environment.

### Install a Python virtual environment

	For Linux/Mac 

	python3 -m venv venv
	source venv/bin/activate

	For Windows 
	
	We assume that you already have installed git-bash.  If so open a git-bash console and :

	ptyhon -m venv venv 
	
	venv\Scripts\activate

### git clone the scripts

	git clone 
	cd Extended_TID_version_2/
	
### install needed modules

ETID uses the following modules

- requests

	pip install requests
	
Or you can install them with the following  :
	
	pip install -r requirements.txt

## Get your Webex Token and ocnfigure your script

- Go to [developer webex](https://developer.webex.com) and login to your account
- Go to [ documentation ] => REST API / Getting Started

Then Search for : **Your Personal Access Token**

Copy your Webex token

Edit the **check.py** script and paste it into the code :

**ACCESS_TOKEN = 'COPY AND PASTE HERE YOUR WEBEX BEARER TOKEN'**

Then run the script and go thru the next instructions : 

	python check.py

A success message should confirm you that everything is OK.


