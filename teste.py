import pandas as pd
import os

print('Informe:')
nome_mecanico = input('Nome do mecânico: ')
linha = {'mecanico': nome_mecanico}
if os.path.exists('teste.xlsx'):
    df = pd.read_excel('teste.xlsx')
    df = pd.concat([df, pd.DataFrame([linha])], ignore_index=True)


