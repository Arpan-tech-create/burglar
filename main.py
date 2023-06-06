from flask import Flask,render_template

app=Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/abt')
def aboutpage():
    return render_template('about.html')


@app.route('/con')
def conpage():
    return render_template('contact.html')
app.run(debug=True)