from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "eureka"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/thanks')
def thanks():
    return render_template('results.html')

@app.route('/processform', methods=['POST'])
def process_form():
    # print(request.form['first_name'])
    # print(request.form['last_name'])
    # print(request.form['address'])

    session['html_first_name'] = request.form['first_name']
    session['html_last_name'] = request.form['last_name']
    session['html_address'] = request.form['address']

    return redirect('/thanks')

if __name__=="__main__":
    app.run(debug=True)