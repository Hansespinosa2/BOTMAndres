#Work around this later

# Connect to Google Sheets
from gspread import authorize
from oauth2client.service_account import ServiceAccountCredentials
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
    
    return excel_data
