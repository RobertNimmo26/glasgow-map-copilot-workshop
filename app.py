
from flask import Flask, render_template_string
import folium

app = Flask(__name__)

@app.route('/')
def glasgow_map():
    # Coordinates for Glasgow city center
    glasgow_coords = [55.8642, -4.2518]
    m = folium.Map(location=glasgow_coords, zoom_start=12)

    # Add Tree Preservation Order polygons from GeoJSON
    import json
    with open("Tree-Preservation-Glasgow.geojson", "r") as f:
        tpo_geojson = json.load(f)
    folium.GeoJson(
        tpo_geojson,
        name="Tree Preservation Orders",
        style_function=lambda x: {
            'fillColor': 'green',
            'color': 'darkgreen',
            'weight': 2,
            'fillOpacity': 0.4
        },
        tooltip=folium.GeoJsonTooltip(fields=["AREANAME", "EVNUMBER"], aliases=["Area:", "Order:"])
    ).add_to(m)

    map_html = m._repr_html_()
    html = f"""
    <html>
        <head><title>Glasgow Map</title></head>
        <body>
            <h2>Map of Glasgow</h2>
            {map_html}
        </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
