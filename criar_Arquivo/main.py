import csv
import random
from datetime import datetime, timedelta

# Configurações iniciais
products = ["Smartphone", "Laptop", "Tablet", "Smartwatch", "Fone de Ouvido"]
start_date = datetime(2020, 1, 1)
end_date = datetime(2025, 3, 25)

# Função para gerar uma data aleatória
def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

# Criar o arquivo CSV
with open('produtos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Product", "Quantity", "Price"])  # Cabeçalhos

    for _ in range(10000):
        date = random_date(start_date, end_date).strftime('%Y-%m-%d')
        product = random.choice(products)
        quantity = random.randint(1, 50)
        price = round(random.uniform(10.0, 1000.0), 2)  # Preço entre 10 e 1000
        writer.writerow([date, product, quantity, price])