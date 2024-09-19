from flask import Flask, render_template, request, redirect, url_for, jsonify


#creating a flask app
app = Flask(__name__, template_folder="templates")

#Flask app routing
@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to the Home Page</h1>"

@app.route("/index", methods=["GET"])
def index():
    return "<h3>Welocme to the index page</h3>"

# Variable rule
@app.route("/marks/<int:score>")
def marks(score):
    return "You  have passed and your score is: " + str(score)


@app.route("/fail/<int:score>")
def fail(score):
    return "You have failed and your score is: " + str(score)


#html page rendering
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template('form.html')
    

@app.route('/calculate', methods=["GET", "POST"])
def calculate():
    if request.method == "GET":
        return render_template('calculate.html')
    else:
        maths =  float(request.form['maths'])
        science =  float(request.form['science'])
        history =  float(request.form['history'])

        average_marks = (maths+science+history)/3

        res = ""
        if average_marks >= 35:
            res = "marks"
        else:
            res = "fail"
        
        return redirect(url_for(res, score = average_marks))   
        #return render_template("calculate.html", score = average_marks)

@app.route('/api', methods=["POST"])
def api_cal():
    data = request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    return jsonify(a_val + b_val)

if __name__ == "__main__":
    app.run(debug=True)