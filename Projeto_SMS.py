# Sempre que trbalhando com Excel mover os docs em excel para past na qual está inserido o projeto .py
import pandas as pd

from twilio.rest import Client

account_sid = "-----------------------"
auth_token = "------------------------"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguém que bateu a meta!!! Vendedor: {vendedor}, com um número de vendas de: {vendas}')
        message = client.messages.create(
            from_="+15077095892",
            to="+5500000000000",
            body=f'No mês de {mes} alguém que bateu a meta!!! Vendedor: {vendedor}, com um número de vendas de: {vendas}')


