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
        'content': 'I am still learning python.  This is some content.  This is some more content.',
        'date_posted': 'April, 21st, 2022'
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


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug="true")
