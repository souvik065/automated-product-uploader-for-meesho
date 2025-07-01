from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active

wb.save('Products.xlsx')

