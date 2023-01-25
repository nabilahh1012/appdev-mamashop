from flask import Flask, render_template, request, redirect, url_for
from Forms import PaymentForm
import shelve, User

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')

@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = PaymentForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")

        user = User.User(create_user_form.namec.data, create_user_form.credit_card.data,
create_user_form.exp_date.data, create_user_form.ccv.data, create_user_form.name.data, create_user_form.remarks.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

#        users_dict = db['Users']
#        user = users_dict[user.get_user_id()]
#        print(user.get_name(), "was stored in user.db successfully with user_id ==",
#user.get_user_id())

        db.close()

        return redirect(url_for('retrieve_payment'))
    return render_template('createUser.html', form=create_user_form)


@app.route('/retrievePayment')
def retrieve_payment():
    users_dict = {}
    db = shelve.open('user.db','r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('retrievePayment.html',count=len(users_list), users_list=users_list)


# @app.route('/read')
# def read():
#     db = shelve.open('user.db', 'r')
#     read = db['User']
#     db.close()
#     return render_template('home.html', read=read)

if __name__ == '__main__':
    app.run()


