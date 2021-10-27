from root import app
from flask import render_template

@app.route('/')
def index():
    return render_template('signin.html')

@app.route('/main')
def main():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)