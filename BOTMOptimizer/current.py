# CURRENT BOTM ROUTES

f_current = []
days_list = list(days.keys())

for day_ind in range(len(days_list)):
    df_today = df_week[day_ind]
    # Name of column with route info for a specific day (e.g., 'MON')
    col_today = next(key for key, value in days_cols.items() if value == day_ind)

    # Define the map centered around BOTM
    temp_fig = folium.Figure(height=500, width=1000)
    temp_map = folium.Map(location=[29.616321, -82.422549], zoom_start=10).add_to(temp_fig)

    folium.Marker(
        location=depot,
        icon=folium.Icon(color="green", icon="bus", prefix='fa')
        # setZIndexOffset=1000
    ).add_to(temp_map)

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
            # popup=row['LOCATION']
        ).add_to(temp_map)

    folium.Marker(
        location=depot,
        icon=folium.Icon(color="green", icon="bus", prefix='fa')
        # setZIndexOffset=1000
    ).add_to(temp_map)

    coords_today = {}

    for index, row in df_today.iterrows():
        vehicle = row[col_today][0]  # vehicle id (a, b, c, etc.)
        coords = (float(row['LONG']), float(row['LAT']))

        if vehicle not in coords_today.keys():
            coords_today[vehicle] = []
            coords_today[vehicle].append((-82.328536, 29.660709))  # start at botm

        coords_today[vehicle].append(coords)

        if '*' in row[col_today]:
            coords_today[vehicle].append((-82.328536, 29.660709))  # add botm stop

    routes_mon = []

    for veh in coords_today:
        coords_today[veh].append((-82.328536, 29.660709))  # end at botm

        finished = (len(coords_today[veh]) >= 4)  # need at least 4 sets of coords
        while not finished:
            coords_today[veh].append((-82.328536, 29.660709))
            finished = (len(coords_today[veh]) >= 4)

        route = ors_client.directions(
            coordinates=coords_today[veh],
            profile='driving-car',
            format='geojson',
            optimize_waypoints=False
        )
        routes_mon.append(route)

    veh_code = {'a': 0, 'b': 1, 'c': 2, 'd': 3}

    def style_function(color):
        return lambda feature: dict(color=color, weight=3, opacity=1)

    colors_list = ['orange', 'blue', 'red', 'green', 'black', 'purple']

    for i in range(len(coords_today)):
        veh = list(veh_code.keys())[i]
        color = colors_list[i]

        gj = folium.GeoJson(
            routes_mon[veh_code[veh]],
            name=veh,
            style_function=style_function(color)
        )

        # route["miles"] = round(route["distance"] / 1000 * 0.621371, 1)
        # route["hrs"] = route["duration"] // 3600
        # route["mins"] = round((route["duration"] % 3600) / 60)

        # gj.add_child(folium.Tooltip(
        #     """<h5>Vehicle {vehicle}</h5>
        #     <b>Distance:</b> {miles} mi <br>
        #     <b>Duration:</b> {hrs} hr {mins} min
        #     """.format(**route)
        # ))
        gj.add_to(temp_map)

    folium.LayerControl().add_to(temp_map)
    f_current.append(temp_fig)
