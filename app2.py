from flask import Flask #引入flask套件 (BSD)
import folium   #地圖套件 (MIT)
import geocoder #座標查詢 (MIT)

app = Flask(__name__)   #代表flask網頁本身

@app.route("/")         #設定route跟目錄執行hello_world()
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/map")
def show_map():
    m = folium.Map()
    # return m._repr_html_()
    return m.get_root().render()


@app.route("/map/<string:city>")
def show_name(city): #變數名稱要跟<>內一樣
    if city:
        gps = geocoder.osm(city).latlng
        m = folium.Map(gps, zoom_start= 16) #zoom_start縮放大小
        folium.Marker(gps,popup=city ).add_to(m) #popup 點擊動作
        return m.get_root().render()
    else:
        m = folium.Map()
        return m.get_root().render()




if __name__=="__main__": 
    app.run(debug=True)  #讓專案可以直接以python app.py方式運行


#flask --app hello run 
# --app 要執行的app
# hello 程式碼的名稱 (ex: hello.py)
