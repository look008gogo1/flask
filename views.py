from flask import Blueprint,request
from flask import render_template
                                                                                                              
views=Blueprint(__name__,"views")
@views.route("/")
def home():
    return render_template("index.html",name="john",base="hah")
@views.route("/<username>")
def profile(username):
   # args=request.args
   # name=args.get('name')

    return render_template("index.html",name=username)
student=Blueprint(__name__,"student")
@student.route("/")
def now():
    return render_template("student.html")
@student.route("/<hname>")
def list(hname):
    return render_template("student.html",name=hname)
