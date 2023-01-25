from wtforms import Form, StringField, DateField, TextAreaField, validators #DateTimeLocalField

class PaymentForm(Form):
    namec = StringField('NAME ON CARD', [validators.Length(min=1, max=150), validators.DataRequired()])
    credit_card = StringField('CREDIT CARD NUMBER', [validators.Length(min=1, max=16), validators.DataRequired()])
    exp_date = DateField('EXPIRY DATE', [validators.DataRequired()], format = '%Y-%m-%d',
default='')
    ccv = StringField('CCV', [validators.Length(min=1, max=3), validators.DataRequired()])
    name = StringField('NAME', [validators.Length(min=1, max=150), validators.DataRequired()])
   # collectdt = DateTimeLocalField('COLLECTION DATE & TIME',[validators.Optional()], format= '%Y-%m-%d %H:%M:%S')
    remarks = TextAreaField('REMARKS', [validators.Optional()])
