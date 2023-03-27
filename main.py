from flask import Flask, render_template, request
import requests
import smtplib
import os

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
    if request.method == "POST":
        MY_EMAIL = os.environ["MY_EMAIL"]
        print(MY_EMAIL)
        MY_PASSWORD = os.environ["MY_PASSWORD"]
        print(MY_PASSWORD)
        TEST_EMAIL = os.environ["TEST_EMAIL"]
        GMAIL_SERVER = "smtp.gmail.com"
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        message = request.form["message"]
        content = f"Name: {name}\n" \
                  f"Email: {email}\n" \
                  f"Phone: {phone}\n" \
                  f"Message: {message}\n"
        with smtplib.SMTP(GMAIL_SERVER) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=TEST_EMAIL,
                                msg=f"Subject: New message\n\n{content}")
        return render_template("contact.html", message_sent=True)
    return render_template("contact.html", message_sent=False)


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

