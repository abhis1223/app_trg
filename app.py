from flask import Flask,render_template,redirect

app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY='opds'
)

@app.route('/', methods=['GET','POST'])
def login():
    user={"name":"Abhishek"}
    return render_template("index.html", user=user)

if __name__ == "__main__":
    app.run(host="0.0.0.0")