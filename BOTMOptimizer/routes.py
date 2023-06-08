from os import truncate
from folium.plugins import BeautifyIcon
import pandas as pd
from gspread import authorize
#from gspread.models import Cell
from oauth2client.service_account import ServiceAccountCredentials
#from google.colab import drive
from pandas._libs.hashtable import value_count
from google_sheets import connect_to_sheets
import re


def process_worksheet():
    # Access Google Sheet
    gclient = connect_to_sheets()
    worksheet = gclient.open("BOTM Database").sheet1
    rows = worksheet.get_all_values()
    columns = rows[0]
    df = pd.DataFrame.from_records(rows[1:], columns=columns)

    # Filter by numerical lat/long and day of the week
    df = df[df['LAT'].apply(lambda x: not re.search("[A-Za-z]", x))]
    df = df[df['LONG'].apply(lambda x: not re.search("[A-Za-z]", x))]
    df = df[(df['LAT'] != '') | (df['LONG'] != '')]

    df_mon = df[df['MON'] != ''].sort_values(by=['MON'])
    df_tues = df[df['TUES'] != ''].sort_values(by=['TUES'])
    df_wed = df[df['WED'] != ''].sort_values(by=['WED'])
    df_thurs = df[df['THURS'] != ''].sort_values(by=['THURS'])
    df_fri = df[df['FRI'] != ''].sort_values(by=['FRI'])
    df_week = [df_mon, df_tues, df_wed, df_thurs, df_fri]

   

    # Additional processing logic or functions can be included here

    # Return or perform further operations with the processed data
    return df_week
