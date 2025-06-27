 from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login')
def login():
    role = request.args.get('role', 'user')
    return render_template("login.html", role=role)

@app.route('/dashboard/user')
def user_dashboard():
    return render_template("user_dashboard.html")

@app.route('/dashboard/shop')
def shop_dashboard():
    return render_template("shop_dashboard.html")

if __name__ == '__main__':
    app.run(debug=True)
