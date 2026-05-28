from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here' # غيّرها لأي نص عشوائي

# قاعدة بيانات وهمية (بدل قاعدة بيانات SQL)
users = {"admin": "1234"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if users.get(username) == password:
            session['user'] = username
            return "تم تسجيل الدخول بنجاح! مرحباً بك يا " + username
        return "اسم المستخدم أو كلمة المرور خطأ!"
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)