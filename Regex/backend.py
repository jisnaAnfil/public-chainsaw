# app.py
from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matched_strings = re.findall(regex_pattern, test_string)
    return render_template('index.html', matched_strings=matched_strings)


@app.route('/validate-email', methods=['GET', 'POST'])
def validate_email():
    if request.method == 'POST':
        email = request.form['email']
        is_valid = validate_email_regex(email)
        return render_template('index.html', email=email, is_valid=is_valid)
    return render_template('index.html')

def validate_email_regex(email):
    # Simple regex pattern to validate email format
    regex_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(regex_pattern, email) is not None


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
