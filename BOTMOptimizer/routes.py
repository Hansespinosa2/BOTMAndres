import pandas as pd
from gspread import authorize
from oauth2client.service_account import ServiceAccountCredentials
from file_connect import connect_to_sheets, connect_to_excel, column_titles, fix_df
import re

def process_worksheet():
    worksheet = connect_to_excel("C:\\Users\\hanse\\Downloads\\BOTM Database.xlsx")
    columns = column_titles("C:\\Users\\hanse\\Downloads\\BOTM Database.xlsx")
    df = fix_df(worksheet)

    df = df[df['LAT'].apply(lambda x: not re.search("[A-Za-z]", str(x)))]
    df = df[df['LONG'].apply(lambda x: not re.search("[A-Za-z]", str(x)))]
    df = df[(df['LAT'] != '') | (df['LONG'] != '')]

    df_mon = df[df['MON'] != ''].sort_values(by=['MON'])
    df_tues = df[df['TUES'] != ''].sort_values(by=['TUES'])
    df_wed = df[df['WED'] != ''].sort_values(by=['WED'])
    df_thurs = df[df['THURS'] != ''].sort_values(by=['THURS'])
    df_fri = df[df['FRI'] != ''].sort_values(by=['FRI'])
    df_week = [df_mon, df_tues, df_wed, df_thurs, df_fri]

    return df_week
