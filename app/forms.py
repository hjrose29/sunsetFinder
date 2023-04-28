from wtforms import Form, StringField, SelectField,IntegerField


class dateForm(Form):
    select = SelectField('Please Enter a Date:')
    search = StringField('(MM/DD/YYYY)')