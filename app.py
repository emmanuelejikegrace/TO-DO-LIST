from flask import Flask, render_template, request

app = Flask(__name__)

tasks = [
    {"name": "learn falsk", "completed": False},
    {"name": "Build to-do app", "completed": False},
    {"name": "Practice python", "completed": False}
]

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form["task"]

    if task.strip() == "":
        return render_template(
            "index_html",
            tasks=tasks,
            message="Task cannot be empty!"
        )

    for existing_task in tasks:
        if existing_task["name"] == task:
            return render_template(
                "index_html",
                tasks=tasks,
                message="Task already exists!"
            )

    tasks.append({"name": task, "completed": False}) 

    return render_template("index.html",tasks=tasks)  

@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    tasks[task_id]["completed"] = True

    return render_template("index.html", tasks=tasks)

@app.route("/about")
def about():
    return "<h1>This is the about page</h1>"    