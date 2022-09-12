# This file contains the forms. Forms are used to communicate with the user: submit data, show data, etc.
# The forms must be imported to the routes module and then they should instanciated and then passed to the route functions
# Once the instance form is passed to the route function, it can be used in the HTML file

# import the Flask Form module
from flask_wtf import FlaskForm
# import the String Field which is similar to HTML text and Submit Field which is used for data transfer
from wtforms import StringField, SubmitField
# import Data Required to validate the requirement of filling empty fields
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
    # Title field: a list of validators can be added to show that this field is required
    title = StringField('Title', validators=[DataRequired()])
    # Submite field
    submit = SubmitField('Submit')


class DeleteTaskForm(FlaskForm):
    # Submite field
    submit = SubmitField('Delete')