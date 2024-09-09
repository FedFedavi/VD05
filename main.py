from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    context = {
        'link': 'Улыбнитесь Каскадеры'
    }
    return render_template("home.html", **context)

@app.route("/home/")
def home():
    context = {
        'link': 'Улыбнитесь Каскадеры'
    }
    return render_template("home.html", **context)

#
@app.route("/about/")
def about():
    context = {
               'link': 'Улыбнитесь Каскадеры'
    }
    return render_template("about.html", **context)



if __name__ == "__main__":
    app.run()

