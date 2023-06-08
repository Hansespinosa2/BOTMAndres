# Add coordinates for new locations (~1 sec / new location)

# Access Google Sheet
worksheet = gclient.open("BOTM Database").sheet1
rows = worksheet.get_all_values()

# Convert to a DataFrame
columns = rows[0]
df = pd.DataFrame.from_records(rows[1:], columns=columns)
new_df = df[(df['LAT'] == '') | (df['LONG'] == '')]

# Calculate missing coordinates
cell_list = []
lat_col = df.columns.get_loc('LAT') + 1
long_col = df.columns.get_loc('LONG') + 1
for index, row in new_df.iterrows():
    cell_list.append(Cell(row=index + 2, col=lat_col, value=find_lat(row['ADDRESS'])))
    cell_list.append(Cell(row=index + 2, col=long_col, value=find_long(row['ADDRESS'])))

if cell_list != []:
    worksheet.update_cells(cell_list)

