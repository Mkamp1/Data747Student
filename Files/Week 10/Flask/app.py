from flask import Flask, render_template, request

app = Flask(__name__)

# --- Home route ---
@app.route('/')
def home():
    return render_template('index.html', course="DATA 747")

# --- About route ---
@app.route('/about')
def about():
    return render_template('about.html')

# --- Form route ---
@app.route('/hello', methods=['GET', 'POST'])
def hello():
    name = None
    if request.method == 'POST':
        name = request.form['username']
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
