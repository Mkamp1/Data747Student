DATA 747 – Week 10 Flask Assignment
Author: Michael Kamp
Date: (Insert Submission Date)

------------------------------------------------------
Description
------------------------------------------------------
This project is a simple Flask web application that demonstrates:
- Creating a Flask route
- Passing a variable from Python to an HTML template
- Displaying that variable in a webpage

The application displays a greeting message when accessed in a web browser.


------------------------------------------------------
Project Structure
------------------------------------------------------

Data747_Week10_Flask_MichaelKamp/
│   app.py               # Main Flask application
│   README.txt           # Project notes and run instructions
│
└── templates/
       index.html        # HTML template that displays the message


------------------------------------------------------
How to Run the Application
------------------------------------------------------

1. Open a terminal or command prompt.

2. Navigate to the project folder:
   cd Data747_Week10_Flask_MichaelKamp

3. Activate your Python environment:
   conda activate data747_env

4. Run the Flask application:
   python app.py

5. Open a web browser and navigate to:
   http://127.0.0.1:5000/


------------------------------------------------------
Notes
------------------------------------------------------
- `app.py` handles the routing and passes the message variable
- `index.html` displays the message using Jinja2 syntax: {{ message }}
- Debug mode is enabled in app.py so the site reloads when changes are made

------------------------------------------------------
End of README
------------------------------------------------------
