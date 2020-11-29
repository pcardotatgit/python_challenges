from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from crayons import blue, green, yellow, white, red, cyan
 
app = Flask(__name__)

AMP_AUTHORIZATION ="Basic ZGVmZzI2NDU4MDY0YTA1ZjFmYXo6MTIzNDU2NzgtNGY5NS00M2Q1LTkwOGQtN2E3ZDQxYWQzODV6"
 
@app.route('/')
def index():
    headers = request.headers
    token = headers['Authorization']
    return "Token:\n" + str(token)

@app.route('/test')
def test():
    return "Sounds Good !"
    
@app.route("/v1/events", methods=['GET'])
def AMP1():
    """Get a list of recent events from Cisco AMP."""
    sha256=request.args['detection_sha256']
    print(cyan(f'SHA256 = {sha256}',bold=True))    
    token = request.headers.get('Authorization')
    print()
    print(cyan('AMP GET All Events for a specific Computer',bold=True))        
    print()
    if token==AMP_AUTHORIZATION and sha256=='01468b1d3e089985a4ed255b6594d24863cfd94a647329c631e4f4e52759f8a9':
        print(green('AMP Authorization correct :'+token,bold=True))
        print(green('SHA256 correct :'+sha256,bold=True))
        return render_template('32.json')       
    else: 
        print(red('WRONG AMP Auth or SHA256 ! :'+token,bold=True))
        return '{"ERROR": {"error cause":"invalid Authentication Basic Token :'+token+' "}}'     

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404 
    
    
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0',port=4000,ssl_context='adhoc')