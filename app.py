from flask import Flask #引入flask套件

app = Flask(__name__)   #代表flask網頁本身

@app.route("/")         #設定route跟目錄執行hello_world()
def hello_world():
    return "<p>Hello, World!</p>"

if __name__=="__main__": 
    app.run(debug=True)  #讓專案可以直接以python app.py方式運行


#flask --app hello run 
# --app 要執行的app
# hello 程式碼的名稱 (ex: hello.py)
