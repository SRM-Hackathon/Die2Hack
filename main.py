from flask import Flask,render_template,url_for
app = Flask(__name__)

# login register part

@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/cregister')
def cregister():
    return render_template('cregister.html')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/slogin')
def slogin():
    return render_template('slogin.html')
app.run(debug=True)