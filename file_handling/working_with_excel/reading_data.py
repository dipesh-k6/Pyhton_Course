import openpyxl

wb = openpyxl.load_workbook("students.xlsx")

ws = wb["students"]

for rows in ws.iter_rows(values_only=True):
    print(rows)
