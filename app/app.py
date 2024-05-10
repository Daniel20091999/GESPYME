from flask import Flask
from flask import render_template

import os 
import sys 
import math 
import random

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")
    #return render_template("menu_admin.html")
    #return render_template("menu_manager.html")
    #return render_template("menu_worker.html")
    #return render_template("create_admin_manager.html")
    #return render_template("menu_worker.html")
    #return render_template("delete_worker.html")
    #return render_template("delete_admin_manager.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)