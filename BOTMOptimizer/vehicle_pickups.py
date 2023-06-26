import openrouteservice as ors


def create_vehicles(MAX_VEHICLES, depot, MAX_CAPACITY):
    vehicles = []
    for idx in range(MAX_VEHICLES):
        vehicles.append(
            ors.optimization.Vehicle(
                id=idx,
                start=list(reversed(depot)),
                end=list(reversed(depot)),
                capacity=[MAX_CAPACITY],
                time_window=[1553241600, 1553284800]  # Fri 8-20:00, expressed in POSIX timestamp
            )
        )
    return vehicles


def create_pickups(df_week, DEFAULT_SERVICE_TIME):
    pickups_week = []
    for df in df_week:
        pickups = []
        pickups_week.append(pickups)
        for pickup in df.itertuples():
            loc_long = float(pickup.LONG)
            loc_lat = float(pickup.LAT)
            pickups.append(
                ors.optimization.Job(
                    id=pickup.Index,
                    location=[loc_long, loc_lat],  # REVERSED #Ask Dr K question about this!!!!!!!!!
                    service=DEFAULT_SERVICE_TIME,
                    amount=[int(pickup.AMOUNT)],
                )
            )
    return pickups_week
