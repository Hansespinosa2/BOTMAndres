

from vehicle_pickups import create_pickups,create_vehicles
import optimize
import create_map
from routes import process_worksheet


 # Global variables used in the code
MAX_VEHICLES = 3
MAX_CAPACITY = 5000
DEFAULT_SERVICE_TIME = 20*60 # Assume 20 minutes at each site
    
# The vehicles are all located at BOTM
depot = [29.660709,-82.328536]
days = {'M': 0, 'T': 1, 'W': 2, 'R': 3, 'F': 4}
days_cols = {'MON': 0, 'TUES': 1, 'WED': 2, 'THURS': 3, 'FRI': 4}


#average time for capacity 5000
#Don't think this is important ask Dr K @ next meeting
Vehicle1T = 52
Vehicle2T = 26
Vehicle3T = 143
avgDuration = (Vehicle1T + Vehicle2T + Vehicle3T)/3
#FIGURE OUT __INIT__

# Assuming you have the necessary variables defined
df_week = process_worksheet()
vehicles = create_vehicles(MAX_VEHICLES, depot, MAX_CAPACITY)
pickups_week = create_pickups(df_week, DEFAULT_SERVICE_TIME)





# Call the optimize function
results = optimize.optimize(pickups_week, df_week, vehicles, depot, days)

# Call the create_map function
f_optimized = create_map.create_map(results, df_week, depot)
f_optimized[days['T']]
