from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/components")
def components():
    return render_template('components.html')


@app.route("/thankyou")
def about():
    return render_template('thankyou.html')


@app.route("/contact.html")
def contact():
    return render_template('contact.html')


@app.route("/works.html")
def works():
    return render_template('works.html')


@app.route("/work")
def work():
    return render_template('work.html')
