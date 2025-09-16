from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/kk')
def hello_world2():  # put application's code here
    data="hello data"
    return render_template("kk.html", data=data)

@app.route('/user/<username>',methods=["get","post"])
def get_user(username):
    return "Hello %s" % username

@app.route('/data',methods=["post","get"])

def test_data():
    # print(request.args)
    # print(request.args.get("a"),request.args.get("b"))
    # print(request.headers)
    # print(request.headers.get("User-Agent"))
    # print(request.data)
    # import json
    # print(json.loads(request.data))
    # print(request.cookies)
    # print(request.cookies.get("token"))
    print(request.form)
    print(request.form.get("username"),request.form.get("password"))

    return "success"

@app.route("/use_template")
def use_template():
    datas=[(1,"name1"),(2,"name2"),(3,"name3")]
    title="學生資料"
    return render_template("use_template.html",datas=datas,title=title)

@app.route("/pvuv")
def pvuv():
    #read file
    data=[]
    with open("./data/pvuv.txt", "r", encoding="utf-8") as fin:
        next(fin)

        for line in fin:
            line = line.strip()
            pdate, pv, uv = line.split("\t")
            data.append((pdate, pv, uv))

    #return html
    return render_template("pvuv.html",data=data)


if __name__ == '__main__':
    app.run()
