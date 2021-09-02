from flask import Flask
from flask import request
from flask import render_template
import subprocess

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def index():

    print(request.method)
    password = open("password.txt", "r").read()
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        print(request.form)
        if(request.form.get('pass') == password):
            if(request.form.get('value') == 'Restart'):
                print('Restarting server')
                subprocess.run('/home/arkserver/arkserver restart', shell=True)
            elif(request.form.get('value') == 'Stop'):
                print('Stopping server')
                subprocess.run('/home/arkserver/arkserver stop', shell=True)
            elif(request.form.get('value') == 'Update'):
                print('Updating server')
                subprocess.run('/home/arkserver/arkserver update', shell=True)
            elif(request.form.get('value') == 'Start'):
                print('Starting  server')
                subprocess.run('/home/arkserver/arkserver start', shell=True)
            return render_template("index.html", data=['Command Sent to Server'])
        return render_template("index.html", data=['Authentication Failed'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
