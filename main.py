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


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        print(request.form["name"])
        print(request.form["email"])
        print(request.form["phone"])
        print(request.form["message"])
        return "<h1>Successfully sent your message</h1>"

# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#     if

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

