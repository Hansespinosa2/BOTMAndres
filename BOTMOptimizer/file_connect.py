from gspread import authorize
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from geocoding import find_lat, find_long
from path_directories import DATABASE_EXCEL


def connect_to_sheets():
    # Define the scope of the API access
    scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

    # Path to your service account credentials JSON file
    credentials_file = "C:\\Users\\hanse\\Downloads\\credentials.json"

    # Create credentials object
    credentials = ServiceAccountCredentials.from_json_keyfile_name(credentials_file, scope)

    # Authorize the client
    gclient = authorize(credentials)
    return gclient


def connect_to_excel(file_path):
    excel_data = pd.read_excel(file_path)
    excel_data = excel_data.fillna("")
    excel_data2 = excel_data.to_numpy()
    fix_df(excel_data2)
    return excel_data.to_numpy()


def column_titles(file_path):
    excel_data = pd.read_excel(file_path)
    return list(excel_data.columns)


def fix_df(worksheet):
    # gclient = connect_to_sheets()
    # Convert to a DataFrame
    columns = column_titles(DATABASE_EXCEL)
    df = pd.DataFrame.from_records(worksheet, columns=columns)
    new_df = df[(df['LAT'] == '') | (df['LONG'] == '')]

    # print(df)
    # print(new_df)
    # Calc missing coordinates
    cell_list = []
    lat_col = df.columns.get_loc('LAT')
    long_col = df.columns.get_loc('LONG')
    # print(long_col)
    # print(lat_col)

    for index, row in new_df.iterrows():
        # df['LAT'] = df.apply(lambda row: find_lat(row['ADDRESS']) if row['LAT'] == '' else row['LAT'], axis=1)
        # cell_list.append(row=index+2, col=lat_col, value=find_lat(row['ADDRESS']))
        df.iloc[index, lat_col] = find_lat(row['ADDRESS'])
        df.iloc[index, long_col] = find_long(row['ADDRESS'])

    return df
