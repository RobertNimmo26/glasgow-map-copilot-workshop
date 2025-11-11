
from flask import Flask, render_template_string
import folium
import json
import hashlib
import os

app = Flask(__name__)

def generate_color_from_text(text):
    """Generate a distinct, visually accessible color from text using hash-based approach."""
    if text is None:
        text = "unknown"
    
    # Use hash to generate consistent color for same text
    hash_hex = hashlib.sha256(text.encode()).hexdigest()
    
    # Use different parts of the hash for hue, saturation, and lightness to reduce collisions
    hue = int(hash_hex[:8], 16) % 360
    saturation = 60 + (int(hash_hex[8:16], 16) % 25)
    lightness = 40 + (int(hash_hex[16:24], 16) % 30)
    
    return f'hsl({hue}, {saturation}%, {lightness}%)'

@app.route('/')
def glasgow_map():
    # Coordinates for Glasgow city center
    glasgow_coords = [55.8642, -4.2518]
    m = folium.Map(location=glasgow_coords, zoom_start=12)

    # Add Tree Preservation Order polygons from GeoJSON
    with open("Tree-Preservation-Glasgow.geojson", "r") as f:
        tpo_geojson = json.load(f)
    
    # Create a mapping of areas to colors for the legend
    area_colors = {}
    for feature in tpo_geojson['features']:
        areaname = feature['properties'].get('AREANAME')
        if areaname and areaname not in area_colors:
            area_colors[areaname] = generate_color_from_text(areaname)
    
    def style_function(feature):
        areaname = feature['properties'].get('AREANAME')
        color = generate_color_from_text(areaname)
        return {
            'fillColor': color,
            'color': color,
            'weight': 2,
            'fillOpacity': 0.5
        }
    
    folium.GeoJson(
        tpo_geojson,
        name="Tree Preservation Orders",
        style_function=style_function,
        tooltip=folium.GeoJsonTooltip(fields=["AREANAME", "EVNUMBER"], aliases=["Area:", "Order:"])
    ).add_to(m)
    
    # Add a custom legend showing area colors
    legend_html = '''
    <div style="position: fixed; 
                top: 10px; right: 10px; width: 300px; height: 400px; 
                background-color: white; border:2px solid grey; z-index:9999; 
                font-size:12px; overflow-y: scroll; padding: 10px;">
    <h4 style="margin-top:0;">Tree Preservation Areas</h4>
    '''
    
    # Sort areas alphabetically for easier lookup
    for area in sorted(area_colors.keys()):
        if area:  # Skip None values
            color = area_colors[area]
            legend_html += f'''
            <div style="margin-bottom: 5px;">
                <span style="display:inline-block; width:20px; height:20px; 
                             background-color:{color}; border:1px solid #333; 
                             vertical-align:middle; margin-right:5px;"></span>
                <span style="vertical-align:middle; font-size:11px;">{area}</span>
            </div>
            '''
    
    legend_html += '</div>'
    m.get_root().html.add_child(folium.Element(legend_html))

    map_html = m._repr_html_()
    html = f"""
    <html>
        <head><title>Glasgow Tree Preservation Map</title></head>
        <body>
            <h2>Glasgow Tree Preservation Orders</h2>
            <p>Each colored area represents a different Tree Preservation Order. Hover over areas for details.</p>
            {map_html}
        </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    # Use environment variable to control debug mode, default to False for production safety
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ('true', '1', 'yes')
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
