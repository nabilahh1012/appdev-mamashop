from wtforms import Form, EmailField, StringField, PasswordField, TextAreaField, validators

class LogInForm(Form):
    username = StringField('Username', [validators.Length(min=5, max=25), validators.DataRequired()])
    # eye_icon = Markup('<i class="icon-eye" id="togglePassword"')
    password = PasswordField('Password', [validators.Length(min=8, max=150), validators.DataRequired()])

class ContactUsForm(Form):
    first_name = StringField('First Name', [validators.Length(min=3, max=25), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=3, max=25), validators.DataRequired()])
    email = EmailField('Email Address', [validators.Email(), validators.DataRequired()])
    phone = StringField('Contact Number', [validators.Length(min=8, max=8), validators.DataRequired()])
    remarks = TextAreaField('Remarks', [validators.Length(max=200), validators.DataRequired()])

class SignUpForm(Form):
    username = StringField('Username', [validators.Length(min=5, max=25), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=8, max=25), validators.DataRequired()])
    phone = StringField('Contact Number', [validators.Length(min=8, max=8), validators.DataRequired()])
