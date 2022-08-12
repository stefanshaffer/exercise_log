from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b8831ce3a91d35dd9088d4a2e7762df8'

posts = [
    {
        'author': 'Stefan',
        'title': 'Learning Python',
        'content': 'I am learning python.  This is some content.  This is some more content.',
        'date_posted': 'April 20th, 2022'
    },
    {
        'author': 'Stefan',
        'title': 'Learning Python 2',
        'content': 'I learned about f strings today and that they are useful for refrencing a class or variable '
                   'inside of a string.  I learned that flask has a lot of built-in functionality like the forms, '
                   'validators and flash messages.',
        'date_posted': 'August, 9th, 2022'
    }
]


@app.route('/')
@app.route('/home')
def home():  # put application's code here
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', "success")
            return redirect(url_for('home'))
    else:
        flash('Login Unsuccesful, please check username and/or password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug="true")
