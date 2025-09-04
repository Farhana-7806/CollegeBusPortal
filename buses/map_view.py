# map_view.py
from flask import Flask, render_template_string
from gps_server import gps_data  # Import shared data

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Bus GPS Tracker</title>
    <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDVlkleGJYdnpV4XVckr17zhmuceoTyvBE"></script>
    <script>
    function initMap() {
        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 6,
            center: {lat: 23.0, lng: 77.0}
        });

        var markers = {{ markers|safe }};
        for (var i = 0; i < markers.length; i++) {
            var m = markers[i];
            new google.maps.Marker({
                position: {lat: m.lat, lng: m.lng},
                map: map,
                label: m.label
            });
        }
    }
    </script>
</head>
<body onload="initMap()">
    <h2>Live GPS Tracker</h2>
    <div id="map" style="height: 600px; width: 100%;"></div>
</body>
</html>
"""

@app.route("/")
def map_view():
    markers = []
    for label, (lat, lng) in gps_data.items():
        markers.append({"label": label, "lat": lat, "lng": lng})
    return render_template_string(HTML_TEMPLATE, markers=markers)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
