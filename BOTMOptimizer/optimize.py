import openrouteservice as ors

def optimize(pickups_week, df_week, vehicles, depot, days):
    optimized_results = []

    days_list = list(days.keys())

    for day_ind in range(len(days_list)):
        pickups_today = pickups_week[day_ind]
        df_today = df_week[day_ind]

        ors_client = ors.Client(key='5b3ce3597851110001cf62489217d34c333d469aa2034e367d70cb0a')
        result = ors_client.optimization(
            jobs=pickups_today,
            vehicles=vehicles,
            geometry=True,
        )

        optimized_results.append(result)

    return optimized_results
