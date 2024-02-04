import os.path
import math
from datetime import datetime

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# Define the variables
SHEET_ID = "16trqF-iA_onzmajYVcLQfmunsiJnXPdyVIm01SRRAnM"
SHEET_RANGE = "Pagina1!A1:H"

# Log
def log(msg):
    print(f"{datetime.now().isoformat()} - {msg}")

# Calculate the student's situation
def calcular_situacao(faltas, media, total_classes):
    if faltas > total_classes * 0.25:
        return "Reprovado por Falta"
    elif media < 5:
        return "Reprovado por Nota"
    elif media < 7:
        return "Exame Final"
    else:
        return "Aprovado"

# Calculate the final approval grade
def calcular_naf(media):
    return math.ceil((10 - media) * 2)

# Main function
def main():
    log("Starting the application...")

    # Authentication with Google Sheets
    try:
        credentials = _get_credentials()
        service = build("sheets", "v4", credentials=credentials)
    except HttpError as err:
        log(f"Authentication error: {err}")
        return

    # Reading the data from the spreadsheet
    try:
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SHEET_ID, range=SHEET_RANGE).execute()
        values = result.get("values", [])
    except HttpError as err:
        log(f"Error reading the spreadsheet: {err}")
        return

    # Processing the data
    log("Processing data...")
    data_to_insert = []
    total_classes = int(values[1][0].split(": ")[1])  # Get the total number of classes from the spreadsheet
    for i, row in enumerate(values):
        if i < 3:  # Skip the first three rows
            continue
        if len(row) >= 6:  # Check if the row has enough elements
            try:
                matricula = row[0]
                aluno = row[1]
                faltas = int(row[2])
                p1 = float(row[3])
                p2 = float(row[4])  
                p3 = float(row[5])
                media = round((p1 + p2 + p3) / 3, 2)
                situacao = calcular_situacao(faltas, media, total_classes)
                naf = 0 if situacao != "Exame Final" else calcular_naf(media)
                log(f"- {matricula} - {aluno}: {situacao}, NAF: {naf}")
                data_to_insert.append([situacao, naf])
            except ValueError:
                log(f"Error: Invalid row - {row}")

    # Writing the results to the spreadsheet
    try:
        body = {
            "values": data_to_insert
        }
        for i, row_data in enumerate(data_to_insert, start=4):
            range_to_write = f"Pagina1!G{i}:H{i}"
            body = {
                "values": [row_data]
            }
            sheet.values().update(
                spreadsheetId=SHEET_ID,
                range=range_to_write,
                valueInputOption="USER_ENTERED",
                body=body
            ).execute()
        log("Data successfully inserted!")
    except HttpError as err:
        log(f"Error writing to the spreadsheet: {err}")

# Get Google credentials
def _get_credentials():
    if os.path.exists("token.json"):
        return Credentials.from_authorized_user_file("token.json", SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "client_secret.json", SCOPES
        )
        return flow.run_local_server(port=0)

# Start of the application
if __name__ == "__main__":
    main()
