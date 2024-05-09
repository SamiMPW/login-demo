from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    else:
        username = request.form["user"]
        password = request.form["password"]
        if username == None:
            return render_template("index.html")
        elif username == "sami"and password == "password":
           return "Hello " + username
        else:
          return "User not recognised"

app.route("/signup")
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    else:
        f = open("login.txt" , "w")
        f.write(request.form["un"])
        f.write("\n")
        f.write(request.form[""])
        f.write("")