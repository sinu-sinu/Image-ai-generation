import gspread
from oauth2client.service_account import ServiceAccountCredentials
from config.settings import SERVICE_ACCOUNT_PATH

def get_gspread_client():
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        SERVICE_ACCOUNT_PATH, scope
    )
    
    client = gspread.authorize(creds)
    return client


