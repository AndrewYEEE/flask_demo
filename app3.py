from flask import Flask, render_template #引入樣板
import yfinance as yf # yahoo的股票資料 (https://echarts.apache.org/examples/zh/index.html)

app = Flask(__name__)   #代表flask網頁本身

@app.route("/")         #設定route跟目錄執行hello_world()
def index():
    content = '<p>Hello Tester</p>'
    return render_template('index.html',content=content) #指定使用templates裡的樣板檔案


@app.route("/stock")        #股票圖表範例
def show_stock():
    df = yf.download("^TWII")#抓台灣股價
    df = df.reset_index()   #設定index
    # df.head()             #列出前幾筆資料
    df['Date'] = df['Date'].dt.strftime('%Y/%m/%d') #日期格式轉換
    mydata = df[['Date','Open','Close','Low','High']].tail(100).values.tolist()
    return render_template('stock.html',mydata=mydata, title="台灣股票加權指數" )    


@app.route("/stock/<symbol>") #股票圖表自定義查詢範例
def show_symbol(symbol):
    df = yf.download(symbol)#抓台灣股價
    df = df.reset_index()   #設定index
    # df.head()             #列出前幾筆資料
    df['Date'] = df['Date'].dt.strftime('%Y/%m/%d') #日期格式轉換
    mydata = df[['Date','Open','Close','Low','High']].tail(100).values.tolist()
    return render_template('stock.html',mydata=mydata, title=symbol )    


if __name__=="__main__": 
    app.run(debug=True)  #讓專案可以直接以python app.py方式運行

