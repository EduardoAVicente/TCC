import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Dados fornecidos
data = {
    "site": [
        "amazon", "amazon", "amazon", "amazon", "amazon", "amazon", "amazon", "amazon",
        "amazon", "amazon", "amazon", "amazon", "amazon", "amazon", "magazine luiza",
        "magazine luiza", "magazine luiza", "magazine luiza", "mercadolivre", "mercadolivre",
        "mercadolivre", "mercadolivre"
    ],
    "price": [
        976.67, 949.00, 969.00, 969.00, 998.89, 898.00, 949.00, 976.67,
        998.89, 969.00, 969.00, 949.00, 898.00, 949.00, 836.10, 899.10,
        836.10, 863.10, 949.00, 929.00, 929.00, 899.65
    ],
    "to_char": [
        "02/09", "24/11", "01/09", "02/09", "02/09", "08/09", "03/09", "02/09",
        "02/09", "02/09", "01/09", "24/11", "08/09", "03/09", "06/09", "24/11",
        "29/09", "13/07", "24/11", "01/08", "02/09", "06/09"
    ]
}

# Criando um DataFrame
df = pd.DataFrame(data)

# Convertendo a coluna 'to_char' para datetime para ordenação
df['to_char'] = pd.to_datetime(df['to_char'], format='%d/%m')

# Agrupando por site e data, calculando a média dos preços
df_grouped = df.groupby(['site', 'to_char']).mean().reset_index()

# Ordenando os dados por data
df_grouped = df_grouped.sort_values(by='to_char')

# Criando o gráfico
plt.figure(figsize=(12, 6))
for site in df_grouped['site'].unique():
    site_data = df_grouped[df_grouped['site'] == site]
    plt.plot(site_data['to_char'], site_data['price'], marker='o', label=site)

# Configurando o formato do eixo X para exibir apenas dia/mês
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m'))

# Configurando o gráfico
plt.title('Samsung Galaxy A15 5G Tela de 6.5" 90Hz 128GB Dual Chip', fontsize=14)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Preço (R$)', fontsize=12)
plt.legend(title='e-commerces', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()

# Exibir o gráfico
plt.show()
