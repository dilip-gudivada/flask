from flask import render_template, redirect, flash, url_for, request
from app import app, utils
from app.forms import LoginForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('home'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/PMOForm', methods=['GET', 'POST'])
def pmoform():
    if request.method == "POST":
        details = request.form
        firstname = details.get('first_name')
        lastname = details.get('last_name')
        emailid = details.get('email')
        telephone = details.get('telephone')
        print(firstname + ',' + lastname + ',' + emailid + ',' + telephone)
        region = 'Europe'
        market = 'poland'
        query = "INSERT INTO pmo_test_1(region,market) VALUES ('Europe','Poland')"
        cursor, conn = utils.db_connect()
        cursor.execute(query)
        conn.commit()
        return 'success'
    return render_template('PMOForm.html')
