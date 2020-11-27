import folium

def createMap():
    map = folium.Map(location=[38.50, -99.10], zoom_start=5)
    map.save("E:\\mapExercise\\mapExercise.html")

createMap()