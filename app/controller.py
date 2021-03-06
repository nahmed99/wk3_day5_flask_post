from flask import render_template, request, redirect
from app import app
# In the following line, we can import the function separately because it is NOT from a class!
from app.models.todo_list import tasks, add_new_task
from app.models.task import Task


# Controller routes match HTTP routes TO functions.

# The controller sits and listens, waiting for requests that will come in

# This defaults to a GET request
@app.route('/') # This listens for 'requests' to the home/root
def index():
    # This and other below are normal python functions...
    return render_template('index.html', title="Home", tasks=tasks)


# This defaults to a GET request
@app.route('/info')
def info():
    return render_template('info.html', title='info')


# This defaults to a GET request
@app.route('/create')
def create():
    return render_template('create.html', title='Add New Todo')


#================== HANDLING DATA controllers ===================

# Creating a POST request. This will be a response to the
# data entered in the /create above.
@app.route('/add-task', methods=["POST"])
def add_task():
    print(request.form) # this will be shown in the terminal

    # Take the data from the form
    task_title = request.form["title"]
    task_description = request.form["description"]
    # print("The values extracted from request.form: ", task_title, task_description)

    # make a new instance of a Task using the data as constructor values
    task = Task(task_title, task_description, False)

    # add that new task object to the tasks list
    add_new_task(task)

    # return "Done" 
    return redirect("/") # rather than returning "Done", we redirect to home/root page. We could redirect to formatted 'done' page.
