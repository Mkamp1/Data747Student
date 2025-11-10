import os
import sys
import shutil

# Template structure
template = {
    "app.py": """from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
""",

    "templates/base.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask App</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>

<header>
    <h1>My Flask Website</h1>
</header>

<main>
    {% block content %}{% endblock %}
</main>

</body>
</html>
""",

    "templates/index.html": """{% extends "base.html" %}

{% block content %}
<h2>Welcome to your new Flask project!</h2>
<p>Edit this page in templates/index.html</p>
{% endblock %}
""",

    "static/style.css": """body { font-family: Arial, sans-serif; background: #f7f7f7; margin: 0; }
header { background: #005bbb; color: white; padding: 20px; text-align: center; }
main { padding: 30px; }
""",

    "requirements.txt": "flask"
}

def create_project(name):
    if os.path.exists(name):
        print(f"Folder '{name}' already exists!")
        sys.exit(1)

    os.makedirs(name)
    for path, content in template.items():
        full_path = os.path.join(name, path)
        folder = os.path.dirname(full_path)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

    print(f"✅ Flask project '{name}' created successfully!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: createflask <project_name>")
    else:
        create_project(sys.argv[1])
