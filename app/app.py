from curses.ascii import DC2
from datetime import date
from distutils.util import split_quoted
import shutil
from flask import Flask, render_template,request, redirect
from jsonLoader import *
from forms import dateForm
from SearchByDate import search

app = Flask(__name__,template_folder="templates")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/archive.html",methods=['GET', 'POST'])
def archive():
    toDisplay = "/Users/henry/Documents/sunsetFinder/toDisplay/"
    for i in os.listdir(toDisplay):
        resizeImage(toDisplay, i, i)
        encoded, date = toDisplayToJson(toDisplay, i)
        update_json(encoded, date)
        shutil.move(toDisplay + i, "/Users/henry/Documents/sunsetFinder/app/Archive/" + i)

    images, dates = getImages("archive.json")
    

    spot = dateForm(request.form)
    if request.method == 'POST':

        if request.form.get("Date") == "":
            return render_template('archive.html', c0=zip(images[0], dates[0]), c1=zip(images[1], dates[1]), c2=zip(images[2], dates[2]), c3=zip(images[3], dates[3]))
        date = request.form.get("Date")
        print(date.split('/'))
        month, day, year = date.split('/')
        formatted_date = year + "-" + month + "-" + day
        print(formatted_date)
        images = search(formatted_date, "archive.json")
        count = 0
        img0 = []
        img1 = []
        img2 = []
        img3 = []
        
        date0 = []
        date1 = []
        date2 = []
        date3 = []
        if (images == None):
            return render_template('archive.html', c0=zip(images[0], dates[0]), c1=zip(images[1], dates[1]), c2=zip(images[2], dates[2]), c3=zip(images[3], dates[3]))
        while count < len(images):
            if(count + 1 % 4 != 0):
                img3.append(images[count]["image_name"])
                date3.append(images[count]["date_taken"])
            elif(count + 1 % 3 != 0):
                img2.append(images[count]["image_name"])
                date2.append(images[count]["date_taken"])
            elif(count + 1 % 2 != 0):
                img1.append(images[count]["image_name"])
                date1.append(images[count]["date_taken"])
            else:
                img0.append(images[count]["image_name"])
                date0.append(images[count]["date_taken"])
            count += 1
        return render_template('archive.html', c0=zip(img3,date3), c1=zip(img2, date2), c2=zip(img1, date1), c3=zip(img0, date0))
            
        
   
    
    return render_template('archive.html', c0=zip(images[0], dates[0]), c1=zip(images[1], dates[1]), c2=zip(images[2], dates[2]), c3=zip(images[3], dates[3]))

@app.route("/aboutUs.html")
def aboutUs():
    return render_template('aboutUs.html')


if __name__ == "__main__":
    app.run()