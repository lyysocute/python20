from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello world!</h1>'

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',n=name)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html')