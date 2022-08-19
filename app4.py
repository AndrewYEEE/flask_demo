from flask import Flask, render_template #引入樣板
import plotly.express as px #plotly套件

app = Flask(__name__)   #代表flask網頁本身

@app.route("/")         #設定route跟目錄執行hello_world()
def index():
    df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
    df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
    fig = px.pie(df, values='pop', names='country', title='Population of European continent')
    # fig.show()
    return render_template('index2.html',content=fig.to_html(full_html=False))