# Global variables used in the code
MAX_VEHICLES = 3
MAX_CAPACITY = 5000
DEFAULT_SERVICE_TIME = 20 * 60  # Assume 20 minutes at each site

# The vehicles are all located at BOTM
depot = [29.660709, -82.328536]
days = {'M': 0, 'T': 1, 'W': 2, 'R': 3, 'F': 4}
days_cols = {'MON': 0, 'TUES': 1, 'WED': 2, 'THURS': 3, 'FRI': 4}

# Average time for capacity 5000
Vehicle1T = 52
Vehicle2T = 26
Vehicle3T = 143
avg_duration = (Vehicle1T + Vehicle2T + Vehicle3T) / 3
