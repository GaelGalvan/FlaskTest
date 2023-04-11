from flask import Flask,render_template, request

app = Flask(__name__)
def readDetails(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

@app.route("/")
def Home():
    details = readDetails('static/details.txt')
    return render_template("base.html", name = "Gael", aboutMe = details)


@app.route("/form", methods=['GET', 'POST']) 
def formDemo():
    name = None
    if request.method == 'POST':
        name = request.form['name']
        return render_template("base.html", name = name, aboutMe = readDetails('static/formdetails.txt'))
    return render_template('form.html', name = name)

if __name__ == '__main__':
    app.run(debug=True)