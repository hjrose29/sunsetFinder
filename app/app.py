from datetime import date
import shutil
from flask import Flask, render_template,request, redirect
from jsonLoader import *
from forms import dateForm


app = Flask(__name__,template_folder="templates")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/archive.html",methods=['GET', 'POST'])
def archive():
    toDisplay = "/Users/henry/Documents/sunsetFinder/toDisplay/"
    for i in os.listdir(toDisplay):
        encoded, date = toDisplayToJson(toDisplay, i)
        update_json(encoded, date)
        shutil.move(toDisplay + i, "/Users/henry/Documents/sunsetFinder/app/Archive/" + i)

    images = getImages("archive.json")
    search = dateForm(request.form)
    if request.method == 'POST':
        print(request.form("Date"))
        return render_template('archive.html', c0=images[0], c1=images[1],c2=images[2],c3=images[3])
    #dates = getDates("app/templates/archive.json")
    return render_template('archive.html', c0=images[0], c1=images[1],c2=images[2],c3=images[3])

@app.route("/aboutUs.html")
def aboutUs():
    return render_template('aboutUs.html')


if __name__ == "__main__":
    app.run()