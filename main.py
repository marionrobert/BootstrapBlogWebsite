from flask import Flask, render_template, request
import requests

response = requests.get("https://api.npoint.io/5908ca000ec67c1ee3c6")
# print(response.status_code)
all_posts = response.json()
# print(all_posts)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/form-entry", methods=["POST"])
def receive_data():
    pass


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/posts/<int:index>")
def get_post(index):
    returned_post = None
    for post in all_posts:
        if post["id"] == index:
            returned_post = post
    return render_template("post.html", post=returned_post)


if __name__ == '__main__':
    app.run(debug=True)

