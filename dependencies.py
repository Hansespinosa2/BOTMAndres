#Should be moved and worked around
from IPython.utils import io

with io.capture_output() as captured:
    !pip install folium
print("Folium Installation Complete")

with io.capture_output() as captured:
    !pip install openrouteservice
print("OpenRouteService Installation Complete")