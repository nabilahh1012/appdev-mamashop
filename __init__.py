from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateUserForm
from Forms import LogInForm
from Forms import AdminLogInForm
from Forms import ContactUsForm
import shelve, User

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/household')
def household():
    return render_template('household.html')

@app.route('/signUp', methods=['GET', 'POST'])
def sign_up():
    sign_up_form = CreateUserForm(request.form)
    if request.method == 'POST' and sign_up_form.validate():
        users_dict = {}
        db = shelve.open('user.db','c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")

        user = User.SignUp(sign_up_form.first_name.data, sign_up_form.last_name.data, sign_up_form.email.data, sign_up_form.password.data, sign_up_form.phone.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        #Test codes
        users_dict = db['Users']
        user = users_dict[user.get_user_id()]
        print(user.get_first_name(), user.get_last_name(), "was stored in user.db successfully with user_id ==", user.get_user_id())

        db.close()

        return redirect(url_for('log_in'))
    return render_template('signUp.html', form=sign_up_form)

@app.route('/logIn', methods=['GET', 'POST'])
def log_in():
    log_in_form = LogInForm(request.form)
    if request.method == 'POST' and log_in_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")

        user = User.LogIn(log_in_form.email.data, log_in_form.password.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        db.close()

        return redirect(url_for('home'))
    return render_template('logIn.html', form=log_in_form)

@app.route('/retrieveUsers')
def retrieve_users():
    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('retrieveUsers.html', count=len(users_list), users_list=users_list)

@app.route('/updateUser/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
    update_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'w')
        users_dict = db['Users']

        user = users_dict.get(id)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_email(update_user_form.email.data)
        user.set_password(update_user_form.password.data)
        user.set_phone(update_user_form.phone.data)

        db['Users'] = users_dict
        db.close()

        return redirect(url_for('retrieve_users'))
    else:
        users_dict = {}
        db = shelve.open('user.db', 'r')
        users_dict = db['Users']
        db.close()

        user = users_dict.get(id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.email.data = user.get_email()
        update_user_form.password.data = user.get_password()
        update_user_form.phone.data = user.get_phone()

        return render_template('updateUser.html', form=update_user_form)

    return render_template('updateUser.html')

@app.route('/deleteUser/<int:id>', methods=['POST'])
def delete_user(id):
    users_dict = {}
    db = shelve.open('user.db', 'w')
    users_dict = db['Users']

    users_dict.pop(id)

    db['Users'] = users_dict
    db.close()

    return redirect(url_for('retrieve_users'))


@app.route('/contactUs', methods=['GET', 'POST'])
def contact_us():
    contact_us_form = ContactUsForm(request.form)
    if request.method == 'POST' and contact_us_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")

        user = User.ContactUs(contact_us_form.first_name.data, contact_us_form.last_name.data,
contact_us_form.email.data, contact_us_form.phone.data, contact_us_form.feedback.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        # Test codes
        users_dict = db['Users']
        user = users_dict[user.get_user_id()]
        print(user.get_email(), "was stored in user.db successfully with user_id ==", user.get_user_id())

        db.close()


        return redirect(url_for('retrieve_info'))
    return render_template('contactUs.html', form=contact_us_form)

@app.route('/retrieveInfo')
def retrieve_info():
    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('retrieveInfo.html', count=len(users_list), users_list=users_list)

@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run()
