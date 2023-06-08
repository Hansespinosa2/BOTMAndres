import pandas as pd
# Access Google Sheet
from google_sheets import connect_to_sheets

gclient = connect_to_sheets()
BenWorksheet = gclient.open("Thursday Truck Logs Data Analysis").sheet1
rows = BenWorksheet.get_all_values()

# Convert to a DataFrame
columns = rows[0]
Bendf = pd.DataFrame.from_records(rows[1:], columns=columns) 
##new_df = df[(df['LAT'] == '') | (df['LONG'] == '')]

df_thurs = Bendf[Bendf['THURS']!=''].sort_values(by=['THURS'])

Bendf
