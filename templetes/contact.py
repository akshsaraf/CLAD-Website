from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('contact'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        
        # Handle form submission logic here (e.g., save to database, send email, etc.)
        print(f"Name: {name}, Email: {email}, Message: {message}")


        return "Form submitted successfully"
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
