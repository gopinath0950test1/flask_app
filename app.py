from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello():
    if(request.method=="POST"):
        num_value = int(request.form["num_value"])
        result = num_value * num_value
        return render_template("index.html", result=result)
    else:
        return render_template("index.html")

    

if __name__ == "__main__":
    app.run(debug=True)