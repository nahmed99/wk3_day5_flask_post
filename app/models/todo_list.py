from app.models.task import *



task1 = Task("Buy groceries", "Milk, Cheese, Pizza, Fruit", False)
task2 = Task("Learn Python", "Learn an awesome new programming language", True)
task3 = Task("Learn to POST with Flask", "Use an html form to POST data to the back-end", False)
tasks = [task1, task2, task3]


def add_new_task(task):
    tasks.append(task)
