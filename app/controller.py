from flask import render_template, request
from app import app
from app.models.todo_list import tasks, add_new_task
from app.models.task import *


# The controller sits and listens, waiting for requests that will come in

# This defaults to a get request
@app.route('/') # This listens for 'requests' to the home/root
def index():
    return render_template('index.html', title="Home", tasks=tasks)


# This defaults to a get request
@app.route('/info')
def info():
    return render_template('info.html', title='info')


# This defaults to a get request
@app.route('/create')
def create():
    return render_template('create.html', title='Add New Todo')

# This defaults to a get request
@app.route('add')