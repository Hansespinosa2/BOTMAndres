import pandas as pd
from google_sheets import connect_to_excel

# Access Google Sheet
BenWorksheet = connect_to_excel("C\\Users\\hanse\\Downloads\\BOTM Database")
rows = BenWorksheet.get_all_values()

# Convert to a DataFrame
columns = rows[0]
Bendf = pd.DataFrame.from_records(rows[1:], columns=columns)

df_thurs = Bendf[Bendf['THURS'] != ''].sort_values(by=['THURS'])

Bendf
