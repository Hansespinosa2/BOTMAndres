import folium
import openrouteservice as ors
def create_map(results, df_week, depot):
    f_optimized = []

    for day_ind, result in enumerate(results):
        df_today = df_week[day_ind]

        # Define the map centered around BOTM
        temp_fig = folium.Figure(height=500, width=1000)
        temp_map = folium.Map(location=[29.616321, -82.422549], zoom_start=10).add_to(temp_fig)

        folium.Marker(
            location=depot,
            icon=folium.Icon(color="green", icon="bus", prefix='fa')
        ).add_to(temp_map)

        # Plot the locations on the map with more info in the ToolTip
        for index, row in df_today.iterrows():
            lat = float(row['LAT'])
            long = float(row['LONG'])

            tooltip = folium.Tooltip(
                """<h5>{LOCATION} / {ALIAS} </h5>
                <b>Address:</b> {ADDRESS} <br>
                <b>Location:</b> ({LAT}, {LONG}) <br>
                """.format(**row)
            )
          
            folium.Marker(
                location=(lat, long),
                tooltip=tooltip
            ).add_to(temp_map)

        # Add the output to the map
        for color, route in zip(['green', 'red', 'blue'], result['routes']):
            decoded = ors.convert.decode_polyline(route['geometry'])
            gj = folium.GeoJson(
                name='Vehicle {}'.format(route['vehicle']),
                data={
                    "type": "FeatureCollection",
                    "features": [{
                        "type": "Feature",
                        "geometry": decoded,
                        "properties": {"color": color}
                    }]
                },
                style_function=lambda x: {"color": x['properties']['color']}
            )
            
            route["miles"] = round(route["distance"] / 1000 * 0.621371, 1)
            route["hrs"] = route["duration"] // 3600
            route["mins"] = round((route["duration"] % 3600) / 60)

            gj.add_child(folium.Tooltip(
                """<h5>Vehicle {vehicle}</h5>
                <b>Distance:</b> {miles} mi <br>
                <b>Duration:</b> {hrs} hr {mins} min
                """.format(**route)
            ))
            gj.add_to(temp_map)

        folium.LayerControl().add_to(temp_map)
        f_optimized.append(temp_fig)

    return f_optimized
