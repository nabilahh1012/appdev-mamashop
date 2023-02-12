from flask import Flask, render_template, request, redirect, url_for, session
from Forms import LogInForm, ContactUsForm, SignUpForm, PaymentForm, PickUpForm, ProductForm
import shelve, User, Contact

app = Flask(__name__)
app.secret_key = 'any_random_string'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/household')
def household():
    return render_template('household.html')

@app.route('/cleaningProducts')
def cleaning():
    return render_template('cleaningProducts.html')

@app.route('/desc')
def desc():
    return render_template('desc.html')

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

        user = User.LogIn(log_in_form.username.data, log_in_form.password.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        db.close()

        session['user_created'] = user.get_username()

        return redirect(url_for('home'))
    return render_template('logIn.html', form=log_in_form)

@app.route('/retrieveLogIn')
def retrieve_log_in():
    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('home.html', count=len(users_list), users_list=users_list)

@app.route('/contactUs', methods=['GET', 'POST'])
def contact_us():
    contact_us_form = ContactUsForm(request.form)
    if request.method == 'POST' and contact_us_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'c')

        try:
            customers_dict = db['Customers']
        except:
            print("Error in retrieving Customers from customer.db.")

        customer = Contact.ContactUs(contact_us_form.first_name.data, contact_us_form.last_name.data, contact_us_form.email.data, contact_us_form.phone.data, contact_us_form.remarks.data)
        customers_dict[customer.get_contactus_id()] = customer
        db['Customers'] = customers_dict
        db.close()

        return redirect(url_for('retrieve_contact'))
    return render_template('contactUs.html', form=contact_us_form)

@app.route('/retrieveContacts')
def retrieve_contact():
    customers_dict = {}
    db = shelve.open('customer.db', 'r')
    customers_dict = db['Customers']
    db.close()

    customers_list = []
    for key in customers_dict:
        customer = customers_dict.get(key)
        customers_list.append(customer)

    return render_template('retrieveContacts.html', count=len(customers_list), customers_list=customers_list)

@app.route('/deleteCustomer/<int:id>', methods=['POST'])
def delete_customer(id):
    customers_dict = {}
    db = shelve.open('customer.db', 'w')
    customers_dict = db['Customers']

    customers_dict.pop(id)

    db['Customers'] = customers_dict
    db.close()

    return redirect(url_for('retrieve_contact'))

@app.route('/signUp', methods=['GET', 'POST'])
def sign_up():
    sign_up_form = SignUpForm(request.form)
    if request.method == 'POST' and sign_up_form.validate():
        users_dict = {}
        db = shelve.open('user.db', 'c')

        try:
            users_dict = db['Users']
        except:
            print("Error in retrieving Users from user.db.")

        user = User.SignUp(sign_up_form.username.data, sign_up_form.password.data, sign_up_form.phone.data)
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        db.close()

        session['user_created'] = user.get_username()

        return redirect(url_for('log_in'))
    return render_template('signUp.html', form=sign_up_form)

@app.route('/retrieveSignUp')
def retrieve_sign_up():
    users_dict = {}
    db = shelve.open('user.db', 'r')
    users_dict = db['Users']
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('home.html', count=len(users_list), users_list=users_list)

# @app.route('/cart')
# def cart():
#     return render_template('cart.html')

@app.route('/createProduct', methods=['GET', 'POST'])
def create_product():
    create_product_form = ProductForm(request.form)
    if request.method == 'POST' and create_product_form.validate():
        products_dict = {}
        db = shelve.open('product.db', 'c')

        try:
            products_dict = db['Products']
        except:
            print("Error in retrieving Products from product.db.")

        product = User.Product(create_product_form.name.data, create_product_form.quantity.data, create_product_form.price.data, create_product_form.total.data)
        # product = User.Product(create_product_form.name.data, create_product_form.quantity.data, create_product_form.price.data, create_product_form.total.data)
        products_dict[product.get_product_id()] = product
        db['Products'] = products_dict

        # # Test codes
        # products_dict = db['Products']
        # product = products_dict[product.get_product_id()]
        # print(product.get_name(), "was stored in product.db successfully with product_id ==", product.get_product_id())

        db.close()

        # session['product_created'] = product.get_name()
        #
        return redirect(url_for('retrieve_cart'))
    return render_template('createProduct.html', form=create_product_form)

@app.route('/retrieveCart')
def retrieve_cart():
    products_dict = {}
    db = shelve.open('product.db', 'r')
    products_dict = db['Products']
    db.close()

    products_list = []
    for key in products_dict:
        product = products_dict.get(key)
        products_list.append(product)

    return render_template('retrieveCart.html', count=len(products_list), products_list=products_list)

@app.route('/deleteProduct/<int:id>', methods=['POST'])
def delete_product(id):
    products_dict = {}
    db = shelve.open('product.db', 'w')
    products_dict = db['Products']

    products_dict.pop(id)

    db['Products'] = products_dict
    db.close()

    return redirect(url_for('retrieve_cart'))

@app.route('/createPayment', methods=['GET', 'POST'])
def create_payment():
    create_payment_form = PaymentForm(request.form)
    if request.method == 'POST' and create_payment_form.validate():
        payments_dict = {}
        db = shelve.open('payment.db', 'c')

        try:
            payments_dict = db['Payments']
        except:
            print("Error in retrieving Payments from payment.db.")

        payment = User.Payment(create_payment_form.namec.data, create_payment_form.credit_card.data, create_payment_form.exp_date.data, create_payment_form.ccv.data, create_payment_form.name.data, create_payment_form.remarks.data)
        payments_dict[payment.get_payment_id()] = payment
        db['Payments'] = payments_dict
        db.close()

        return redirect(url_for('retrieve_payment'))
    return render_template('createPayment.html', form=create_payment_form)

@app.route('/retrievePayment')
def retrieve_payment():
    payments_dict = {}
    db = shelve.open('payment.db','r')
    payments_dict = db['Payments']
    db.close()

    payments_list = []
    for key in payments_dict:
        payment = payments_dict.get(key)
        payments_list.append(payment)

    return render_template('retrievePayment.html',count=len(payments_list), payments_list=payments_list)

@app.route('/pickUp', methods=['GET', 'POST'])
def pick_up():
    pick_up_form = PickUpForm(request.form)
    if request.method == 'POST' and pick_up_form.validate():
        pickups_dict = {}
        db = shelve.open('pickup.db', 'c')

        try:
            pickups_dict = db['Pickups']
        except:
            print("Error in retrieving Pickups from pickup.db.")

        pickup = User.PickUp(pick_up_form.username.data, pick_up_form.phone.data, pick_up_form.location.data, pick_up_form.timing.data)
        pickups_dict[pickup.get_pickup_id()] = pickup
        db['Pickups'] = pickups_dict

        db.close()

        return redirect(url_for('retrieve_pickUp'))
    return render_template('pickUp.html', form=pick_up_form)

@app.route('/retrievepickUp')
def retrieve_pickUp():
    pickups_dict = {}
    db = shelve.open('pickup.db','r')
    pickups_dict = db['Pickups']
    db.close()

    pickups_list = []
    for key in pickups_dict:
        pickup = pickups_dict.get(key)
        pickups_list.append(pickup)

    return render_template('retrievePickup.html',count=len(pickups_list), pickups_list=pickups_list)

# @app.route('/read')
# def read():
#     db = shelve.open('user.db', 'r')
#     read = db['User']
#     db.close()
#     return render_template('home.html', read=read)





if __name__ == '__main__':
    app.run()

