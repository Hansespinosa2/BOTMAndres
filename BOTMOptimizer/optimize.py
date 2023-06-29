import openrouteservice as ors


def optimize(pickups_week, df_week, vehicles, depot, days):
    optimized_results = []

    days_list = list(days.keys())

    for day_ind in range(len(days_list)):
        pickups_today = pickups_week[day_ind]
        df_today = df_week[day_ind]

        ors_client = ors.Client(key='5b3ce3597851110001cf62489217d34c333d469aa2034e367d70cb0a')
        # ors_client = ors.Client(base_url='https://localhost:8080/ors/v2/optimization')
        result = ors_client.optimization(
            jobs=pickups_today,
            vehicles=vehicles,
            geometry=True,
        )

        optimized_results.append(result)

    return optimized_results


def set_up_global():
    MAX_VEHICLES = 3
    MAX_CAPACITY = 5000
    DEFAULT_SERVICE_TIME = 20 * 60  # Assume 20 minutes at each site

    depot = [29.660709, -82.328536]
    days = {'M': 0, 'T': 1, 'W': 2, 'R': 3, 'F': 4}
    days_cols = {'MON': 0, 'TUES': 1, 'WED': 2, 'THURS': 3, 'FRI': 4}

    Vehicle1T = 52
    Vehicle2T = 26
    Vehicle3T = 143
    avg_duration = (Vehicle1T + Vehicle2T + Vehicle3T) / 3
