## Writing huge data
from openpyxl import Workbook

wb = Workbook(write_only=True)
ws = wb.create_sheet()

# Writing large data efficiently
for i in range(1, 10001):
    ws.append([f"Row {i}", f"Data {i}"])

wb.save("D:\Ankita\Training\Write_only_huge.xlsx")
