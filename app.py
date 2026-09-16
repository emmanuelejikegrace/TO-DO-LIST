from flask import Flask, render_template, request

app = Flask(__name__)

tasks = [ ]

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form["task"]

    if task.strip() == "":
        return render_template("index.html", tasks=tasks, message="Task caonnot be empty!")
    tasks.append(task) 

    return render_template("index.html",tasks=tasks)   

@app.route("/about")
def about():
    return "<h1>This is the about page</h1>"    