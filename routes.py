# from app module, import the app instance
#                , import the db instace
from re import T
from app import app, db
# form flask module, import two other functions for URL and Redirecting
from flask import render_template, redirect, url_for, flash, get_flashed_messages
import forms
# from module models, import the Task class for your data model
from models import Task
# from module datetime, import datetime
from datetime import datetime

# this points to the root folder of the server
# multiple decorators can be used for a function
@app.route('/')
@app.route('/index')
# exectue the following function
def index():
    # the return value of the function can be a simple string
    # return 'Hello world, Ali is in Canada!'
    
    # the return value of the function can be an html string
    # return '<h1>Welcome to my website!\n</h1><h2>my name is Ali Naseri</h2>'
    
    # the return value of the function can be an html template
    # return render_template('index.html')

    # Query the Task class for the stored information and print them on the index page
    tasks_list = Task.query.all()
    return render_template('index.html', tasks=tasks_list)

# routes are set to be compatible with GET by default. In case you need
# to includee POST, you should consider it in the route definition
# the actions must be provided in a list that is called methods
@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    # now that the POST action is activated, we can have access to the forms data
    
    # check if the data exists:
    if form.validate_on_submit():
        # create an instance of the Task class for storing the data
        t = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()
        # print a message using flash
        flash('Task added to the database')
        # return to the index page after recieving data
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


# now it's time to add functionality for editing a task
# we need a new route for edit
# this time, in the route address, there is a second field which is for passing information 
# between the page to the backend
@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    # the edit page is kind of similar to the add page
    # get the task information from the database
    task = Task.query.get(task_id)
    # we should create a form for the communication of the data
    form = forms.AddTaskForm()
    print(task)

    
    # check if the taks exists, maybe someone provides a wrong task id
    if task:
        # if the submission on the form is activated update the data in the database:
        if form.validate_on_submit():
            task.title = form.title.data
            task.date = datetime.utcnow()
            db.session.commit()
            flash('Task has been updated')
            return redirect(url_for('index'))        

        form.title.data = task.title
        # render the edit html page to show the available task data
        return render_template('edit.html', form=form, task_id=task_id)
    else:
        flash('Task was not found.')
    # go to the index page if none of the above happend
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):

    task = Task.query.get(task_id)
    form = forms.DeleteTaskForm()

    
    # check if the taks exists, maybe someone provides a wrong task id
    if task:
        # if the submission on the form is activated update the data in the database:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash('Task has been deleted')
            return redirect(url_for('index'))        


        # render the edit html page to show the available task data
        return render_template('delete.html', form=form, task_id=task_id, title=task.title)
    else:
        flash('Task was not found')
    # go to the index page if none of the above happend
    return redirect(url_for('index'))