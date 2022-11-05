## use google sheet as database through GoogleApi

import gspread
import pprint

gc = gspread.service_account(filename='secret.json')

sheet = gc.open("Legislators").sheet1

# records = sheet.get_all_records()
record = sheet.row_values(6)
pp = pprint.PrettyPrinter()
pp.pprint(record)