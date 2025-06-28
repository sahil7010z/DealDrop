from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # required for session

# --- Home Page ---
@app.route('/')
def home():
    return render_template('index.html')

# ✅ Load additional products section (loaded via fetch in index.html)
@app.route('/products.html')
def products():
    return render_template('products.html')

# --- Login Page ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Simulated login (no DB yet)
        email = request.form['email']
        password = request.form['password']
        role = request.form.get('role', 'user')
        
        # In real app: check email + password from DB
        if email and password:
            session['user'] = email
            session['role'] = role
            if role == 'shop':
                return redirect(url_for('shop_dashboard'))
            else:
                return redirect(url_for('user_dashboard'))
        else:
            return "Invalid login", 401

    role = request.args.get('role', 'user')
    return render_template('login.html', role=role)

# --- User Dashboard (requires login) ---
@app.route('/dashboard/user')
def user_dashboard():
    if 'user' not in session or session.get('role') != 'user':
        return redirect(url_for('login'))
    return render_template('user_dashboard.html')

# --- Shop Dashboard (requires login) ---
@app.route('/dashboard/shop')
def shop_dashboard():
    if 'user' not in session or session.get('role') != 'shop':
        return redirect(url_for('login'))
    return render_template('shop_dashboard.html')

# --- Demo Deals Page (accessible without login) ---
@app.route('/demo')
def demo_page():
    return render_template('demo.html')

# --- Logout ---
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

# --- Run App ---
if __name__ == '__main__':
    app.run(debug=True)
