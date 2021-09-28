import pandas

excel_data_df = pandas.read_excel('testando.xlsx')

json_str = excel_data_df.to_json()

#tuple(json_str)

#print(tuple)

print(json_str)
