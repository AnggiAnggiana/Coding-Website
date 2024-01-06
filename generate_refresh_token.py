from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_ID = ''
CLIENT_SECRET = ''
SCOPE = ['https://www.googleapis.com/auth/gmail.send']

def generate_refresh_token():
    flow = InstalledAppFlow.from_client_secrets_file(
        "D:\\ME\\PROGRAMMING\\PORTFOLIO\\coding_website_credentials.json", scopes=SCOPE
    )
    
    flow.run_local_server(port=0)
    
if __name__ == "__main__":
    generate_refresh_token()