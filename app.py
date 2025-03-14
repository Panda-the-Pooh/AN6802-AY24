from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return(render_template("index.html"))

@app.route("/main", methods=['GET', 'POST'])
def main():
    user_name = request.form.get("q")
    return(render_template("main.html"))


## food expenditure prediction
@app.route("/foodexp", methods=["GET", "POST"])
def foodexp():
    return(render_template("foodexp.html"))

@app.route("/foodexp_pred", methods=["GET", "POST"])
def foodexp_pred():
    q = float(request.form.get("q")) # input should be float
    return(render_template("foodexp_pred.html", r=(q*0.4851)+147.4))


## ethical test
@app.route("/ethical_test", methods=["GET", "POST"])
def ethical_test():
    return(render_template("ethical_test.html"))

@app.route("/test_result", methods=["GET", "POST"])
def test_result():
    answer = request.form.get("answer")
    if answer == "false":
        return(render_template("pass.html"))
    elif answer == "true":
        return(render_template("fail.html"))

if __name__ == "__main__":
    app.run()

