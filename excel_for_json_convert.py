import pandas
import json

nome_arquivo = ('plan_teste.xlsx')
nome_sheet = ('Plan1')

excel_data_df = pandas.read_excel(nome_arquivo, sheet_name=nome_sheet)

json_str = excel_data_df.to_json()

with open (nome_arquivo.replace(".xlsx", ".json"), 'w') as f:
    f.write(json_str)


