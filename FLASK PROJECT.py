from flask import Flask ,render_template,url_for,redirect,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")
@app.route('/success/<name>')
def success(name):
    return "welcome %s"%name

@app.route("/login",methods =['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['input_name']
        return redirect(url_for("success", name = user))
    else:
        user = request.args.get("input_name")
        return redirect(url_for("success",name=user))


if __name__ == '__main__':
    app.run()
