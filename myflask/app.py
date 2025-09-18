from flask import Flask, render_template,request
import json

import db

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
def read_pvuv_data():
    """
    read pv uv data
    :return: list,eld:(pdate,pv,uv)
    """

    data = []
    with open("./data/pvuv.txt", "r", encoding="utf-8") as fin:
        next(fin)

        for line in fin:
            line = line.strip()
            pdate, pv, uv = line.split("\t")
            data.append((pdate, pv, uv))
    return data
@app.route("/pvuv")
def pvuv():
    #read file
    data=read_pvuv_data()

    #return html
    return render_template("pvuv.html",data=data)

@app.route("/show_add_user")
def show_add_user():
    return render_template("/show_add_user.html")

@app.route("/do_add_user",methods=["post"])
def do_add_user():
    print(request.form)
    name=request.form.get("name")
    sex = request.form.get("sex")
    age = request.form.get("age")
    email = request.form.get("email")
    sql=f"""
         insert into user(name,sex,age,email)
         values("{name}","{sex}",{age},"{email}")
    """
    print(sql)
    db.insert_or_update_data(sql)
    return "success"


@app.route("/getjson")
def getjson():
    # read file
    data=read_pvuv_data()

    #return html
    return json.dumps(data)

@app.route("/show_users/")
def show_user_list():
    sql = "select id,name from user"
    datas = db.query_data(sql)
    return render_template("/show_users.html", datas=datas)


@app.route("/show_user/<user_id>")
def show_user(user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        return render_template("error.html", message="用戶 ID 必須是整數")

    sql = "SELECT * FROM user WHERE id = %s"
    datas = db.query_data(sql, (user_id,))

    if not datas:
        return render_template("error.html", message="查無此用戶")

    user = datas[0]
    return render_template("show_user.html", user=user)


if __name__ == '__main__':
    app.run()
