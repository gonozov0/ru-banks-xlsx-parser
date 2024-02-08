from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import openpyxl

# Путь к вашему файлу credentials.json
SERVICE_ACCOUNT_FILE = 'data/avid-sphere-413708-c20f667d42e2.json'

# Скопируйте и вставьте сюда ID вашей Google Таблицы
SPREADSHEET_ID = '1fExaP4qp64vZsoGyN1Fx7l8IznGkl-13AkEczeepW5c'

# Если вы изменяли scope, не забудьте заменить их здесь
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Аутентификация и создание сервиса
creds = None
creds = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

service = build('sheets', 'v4', credentials=creds)


# Функция для чтения данных из файла Excel
def read_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    data = []

    for row in sheet.iter_rows(min_row=3):  # предполагается, что первая строка - заголовки
        date_of_operation = row[1].value
        amount = row[11].value
        payment_purpose = row[12].value
        if not (date_of_operation or amount or payment_purpose):
            continue
        if date_of_operation:
            date_of_operation = date_of_operation.strftime('%Y-%m-%d')
        data.append([date_of_operation, amount, payment_purpose])

    return data


# Функция для обновления данных в Google Таблице
def update_data_in_sheet(data, sheet_name, start_cell):
    range_name = f'{sheet_name}!{start_cell}'  # Формируем строку диапазона
    body = {
        'values': data
    }
    result = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, range=range_name,
        valueInputOption='USER_ENTERED', body=body
    ).execute()
    print(f"{result.get('updatedCells')} cells updated.")


# Указываем путь к вашему файлу Excel
excel_file_path = 'data/40802810320000013430 044525104(01.01.2024 - 31.01.2024), Входящие.xlsx'

# Чтение данных из файла Excel
excel_data = read_excel(excel_file_path)
print(excel_data)

# Добавляем данные в Google Таблицу на лист "Транзакции" начиная с ячейки G5
update_data_in_sheet(excel_data, 'Транзакции', 'G5')
