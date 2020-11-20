from flask import render_template
from app import app
from app.models.todo_list import tasks

@app.route('/') # This listens for 'requests' to the home/root
def index():
    return render_template('index.html', title="Home", tasks=tasks)


@app.route('/info')
def info():
    return render_template('info.html', title='info')