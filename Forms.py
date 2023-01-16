from wtforms import Form, StringField, EmailField, PasswordField, TextAreaField, validators

class CreateUserForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = StringField('Email', [validators.Length(min=1, max=150), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=1, max=150), validators.DataRequired()])
    phone = StringField('Telephone', [validators.Length(min=1, max=150), validators.DataRequired()])

class LogInForm(Form):
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(max=128), validators.DataRequired()])

class AdminLogInForm(Form):
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(max=128), validators.DataRequired()])

class ContactUsForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    phone = StringField('Telephone', [validators.Length(min=8, max=8), validators.DataRequired()])
    feedback = TextAreaField('Queries', [validators.Length(max=200), validators.DataRequired()])
