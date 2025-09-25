import random
from datetime import datetime, timedelta

#manual
vendas_manuais = [
    {"id": 1, "produto": "Camisa", "quantidade": 2, "preço": 59.90, "data": "2025-01-30"},
    {"id": 2, "produto": "Tênis", "quantidade": 1, "preço": 249.90, "data": "2025-05-30"},
    {"id": 3, "produto": "Calça", "quantidade": 3, "preço": 129.90, "data": "2025-05-05"},
    {"id": 4, "produto": "Jaqueta", "quantidade": 4, "preço": 199.90, "data": "2025-04-24"},
    {"id": 5, "produto": "Bermuda", "quantidade": 7, "preço": 89.90, "data": "2025-03-30"},
    {"id": 6, "produto": "Blusa", "quantidade": 5, "preço": 79.90, "data": "2025-02-27"},
    {"id": 7, "produto": "Salto", "quantidade": 2, "preço": 556.78, "data": "2025-01-18"},
    {"id": 8, "produto": "Sapatilha", "quantidade": 3, "preço": 99.95, "data": "2025-02-09"},
    {"id": 9, "produto": "Bota", "quantidade": 8, "preço": 255.99, "data": "2025-01-12"},
    {"id":10, "produto": "Camiseta", "quantidade": 15, "preço": 25.95, "data": "2025-01-07"},
    {"id": 11, "produto": "Saia", "quantidade": 20, "preço": 49.99, "data": "2025-04-15"},
]

#automaticamente
#gerar data aleatória
def gerar_data_aleatoria():
    hoje = datetime.today() #pega a data de hoje
    dias = random.randint(0, 180)  #gera um número de 0 a 180 dias
    data = hoje - timedelta(days=dias)  #subtrai esses dias da data de hoje
    return data.strftime('%Y-%m-%d')  #converte o objeto datetime para uma string no formato AAAA-MM-DD

nomes_produtos = [
    "Camisa", "Tênis", "Calça", "Jaqueta", "Bermuda", "Blusa",
    "Salto", "Sapatilha", "Bota", "Camiseta", "Saia", "Meia",
    "Boné", "Moletom", "Vestido", "Sandália", "Chinelo", "Blazer"
]

#inserindo dados automaticamente
vendas_automaticas = []

for i in range(12, 68):
    venda = {
        "id": i,
        "produto": random.choice(nomes_produtos), #escolhe um produto aleatoriamente da lista
        "quantidade": random.randint(1, 55), #gera um número inteiro aleatório entre dois valores
        "preço": round(random.uniform(30, 600), 2), #gera um número decimal aleatório entre dois valores 
        "data": gerar_data_aleatoria()
    }
    vendas_automaticas.append(venda)

todas_vendas = vendas_manuais + vendas_automaticas


import psycopg2

# conecta ao banco PostgreSQL
conn = psycopg2.connect(
    dbname="projeto2",
    user="user",
    password="123456",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

for venda in todas_vendas:
    cursor.execute("""
        INSERT INTO vendas (id, produto, quantidade, preco, data)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING
    """, (venda["id"], venda["produto"], venda["quantidade"], venda["preço"], venda["data"]))

# salva alterações
conn.commit()
conn.close()