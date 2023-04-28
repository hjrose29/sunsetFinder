from datetime import date
from flask import Flask, render_template,request, redirect
from jsonLoader import *
from forms import dateForm


app = Flask(__name__,template_folder="templates")

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/archive.html",methods=['GET', 'POST'])
def archive():
    images = getImages("archive.json")
    search = dateForm(request.form)
    if request.method == 'POST':
        print(request.form("Date"))
        return render_template('archive.html', c0=images[0], c1=images[1],c2=images[2],c3=images[3])
    #dates = getDates("app/templates/archive.json")
    return render_template('archive.html', c0=images[0], c1=images[1],c2=images[2],c3=images[3])

if __name__ == "__main__":
    app.run()