from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug="true")
