## use google sheet as database through GoogleApi

import gspread
import pprint

gc = gspread.service_account(filename='secret.json')

sheet = gc.open("Legislators").sheet1

# records = sheet.get_all_records()
# update_cell(x, y , value)
# insert_row(values, x)
# delete_row
row_record = sheet.row_values(6)
col_record = sheet.col_values(3)
pp = pprint.PrettyPrinter()
pp.pprint(col_record)