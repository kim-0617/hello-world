from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")
ws = wb.active

# 삽입을 누르면 위에 셀하나가 삽입된다. (그 위치가 비워진다)
# ws.insert_rows(8)
# ws.insert_rows(8, 5) # 8번째 줄 위치에 5줄 추가

# ws.insert_cols(2) # B열 비워짐
ws.insert_cols(2,3) # B부터 3칸 비워라

# wb.save("sample_rows.xlsx")
wb.save("sample_cols.xlsx")