# Challenge

This challenge is an AMP Threat Hunting challenge.

We assume that you have an AMP for endpoint account.   

**Connect to it and Activate Your Demo Data.**

** And then Create a New client API **

Here is an observable : **01468b1d3e089985a4ed255b6594d24863cfd94a647329c631e4f4e52759f8a9** 

Question 1 : How many Endpoints are infected in your organization by this observable ?

Question 2 : What are the infected Endpoints hostnames ?

## Your Mission

Write a python script which gives you the answer what ever the AMP observable is.

The **solution** Folder contains an example of solution.   But you have to troubleshoot the script

Go to : 

https://api-docs.amp.cisco.com/

And figure out what is the AMP API URL endpoint which can help you to get the answer.

# AMP simulator Backend

If you don't have an AMP demo Account, you can use the AMP backend simulator located into the **amp_simulator** folder

## AMP backend Simulator Installation

Change directory to the directory where is locatef the AMP backend Simulator **.../amp_simulator**.

### Install and start a Python virtual environment

For Linux/Mac 

	python3 -m venv venv
	source bin activate

For Windows 
	
We assume that you already have installed git-bash.  If so open a git-bash console and type the 2 following commands :

	python -m venv venv 
	venv\Scripts\activate
	
### install needed modules
	
	python -m pip install --upgrade pip
	pip install -r requirements.txt

### Run the simulator

	python amp_sim.py
	
You should see the server start. It listen on https 4000.	
	
	(venv) C:\Users\pcardot\Documents\tests\01_amp_challenge\amp_simulator>python amp_sim.py
	 * Serving Flask app "amp_sim" (lazy loading)
	 * Environment: production
	   WARNING: This is a development server. Do not use it in a production deployment.
	   Use a production WSGI server instead.
	 * Debug mode: on
	 * Restarting with stat
	 * Debugger is active!
	 * Debugger PIN: 162-768-494
	 * Running on https://0.0.0.0:4000/ (Press CTRL+C to quit)

### Test the AMP Backend Simulator

Go to the **test_the_amp_backend** folder and run the **test_amp_backend.py** script.

The correct result is :

	{'Simulator State': ['OK']}

# You are ready to go to the challenge

A solution python script template is available for you.

Go to the **solution** folder.

- First open the **environment_api_keys.py** script and assign the correct **AMP_API_KEY** and **AMP_CLIENT_ID**
- Second run the **student_code.py** file and follow the instructions

## API keys for the AMP Backend Simulator

The **AMP_API_KEY** and **AMP_CLIENT_ID** needed for the AMP simulator are already in the **environment_api_keys.py** file.  You just have to uncomment them

## Bonus Challenge

Send the answers into your Webex Team Room

