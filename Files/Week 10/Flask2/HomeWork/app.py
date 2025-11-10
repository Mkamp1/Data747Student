from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    message = "Hello Data 747 class — Created by Michael Kamp"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
