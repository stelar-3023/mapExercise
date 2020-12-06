import folium
import requests




    
def createMap():
    map = folium.Map(location=[38.50, -99.10], zoom_start=5, tiles="Stamen Terrain")
    
    fg = folium.FeatureGroup(name="My Map")
    fg.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a marker", icon=folium.Icon(color="green")))
    map.add_child(fg)
    
    map.save("E:\\mapExercise\\mapExercise.html")

createMap()