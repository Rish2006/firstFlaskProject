from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [

{
    'author': 'Rishitest',
    'title': 'Test Blog post',
    'content': 'test content',
    'date_posted': 'July 14, 2019'
}, 
{   'author': 'Rishitest 2',
    'title': 'Test Blog post 2',
    'content': 'test content 2',
    'date_posted': 'July 15, 2019'
    }

]


@app.route("/homepage")
@app.route("/")
def mainPage():
    return render_template('main.html', posts = posts)

@app.route("/about")
def aboutPage():
    return render_template('about.html')
if __name__=='__main__':
    app.run(debug=True)