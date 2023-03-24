from flask import Flask, render_template
import requests

response = requests.get("https://api.npoint.io/5908ca000ec67c1ee3c6")
print(response.status_code)
all_posts = response.json()
print(all_posts)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)

