from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def pageFirst():
 return "Welcome to the First Page!"

@app.route('/myHome')
def home():
 return render_template('index.html')

@app.route('/about')
def about():
 return render_template('aboutus.html')

@app.route('/membership')
def me():
 return render_template('membership.html')

if __name__ == '__main__':
 app.run(debug=True)