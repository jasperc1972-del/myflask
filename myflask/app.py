from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/kk')
def hello_world2():  # put application's code here
    data="hello data"
    return render_template("kk.html", data=data)


if __name__ == '__main__':
    app.run()
