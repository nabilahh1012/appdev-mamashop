from wtforms import Form, EmailField, StringField, PasswordField, TextAreaField, IntegerField, DateField, validators

class LogInForm(Form):
    username = StringField('Username', [validators.Length(min=5, max=25), validators.DataRequired()])
    # eye_icon = Markup('<i class="icon-eye" id="togglePassword"')
    password = PasswordField('Password', [validators.Length(min=8, max=150), validators.DataRequired()])

class ContactUsForm(Form):
    first_name = StringField('First Name', [validators.Length(min=3, max=25), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=3, max=25), validators.DataRequired()])
    email = EmailField('Email Address', [validators.Email(), validators.DataRequired()])
    phone = IntegerField('Contact Number', [validators.NumberRange(min=11111111, max=99999999), validators.DataRequired()])
    remarks = TextAreaField('Remarks', [validators.Length(max=200), validators.DataRequired()])

class SignUpForm(Form):
    username = StringField('Username', [validators.Length(min=5, max=25), validators.DataRequired()])
    password = PasswordField('Password', [validators.Length(min=8, max=25), validators.DataRequired()])
    phone = IntegerField('Contact Number', [validators.NumberRange(min=11111111, max=99999999), validators.DataRequired()])

class PaymentForm(Form):
    namec = StringField('Name On Card', [validators.Length(min=1, max=150), validators.DataRequired()])
    credit_card = StringField('Credit Card Number', [validators.Length(min=1, max=16), validators.DataRequired()])
    exp_date = DateField('Expiry Date', [validators.DataRequired()], format = '%Y-%m-%d', default='')
    ccv = StringField('CCV', [validators.Length(min=1, max=3), validators.DataRequired()])
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
   # collectdt = DateTimeLocalField('COLLECTION DATE & TIME',[validators.Optional()], format= '%Y-%m-%d %H:%M:%S')
    remarks = TextAreaField('Remarks', [validators.Optional()])

class PickUpForm(Form):
    username = StringField('Username', [validators.Length(min=5, max=25), validators.DataRequired()])
    phone = StringField('Contact Number', [validators.Length(min=8, max=8), validators.DataRequired()])
    location = StringField('Location', [validators.DataRequired()])
    timing = StringField('Timing', [validators.DataRequired()])

