# Carregar o conjunto de dados Titanic
import seaborn as sns
import pandas as pd
titanic = sns.load_dataset('titanic')
# Definindo características (features) e variável alvo (target)
X = titanic.drop(columns=['survived']).dropna()  # Características
y = titanic['survived'][X.index]  # Variável alvo

# Codificar variáveis categóricas
X = pd.get_dummies(X, drop_first=True)

# Exibir as colunas do DataFrame X
#print("Colunas disponíveis em X:")
#print(X.columns.tolist())

#print(titanic.info)
# Se as colunas codificadas para sexo forem diferentes, ajuste a seleção
selected_columns = X[['pclass', 'age', 'alone']] 
selected_y = y.reset_index(drop=True)

# Renomear colunas para maior clareza
selected_columns.columns = ['Classe', 'Idade', 'Sozinho']

# Exibir os dados formatados
result_df = pd.concat([selected_columns, selected_y.rename('Sobreviveu')], axis=1)

# Filtrar para mostrar apenas as pessoas que sobreviveram (Sobreviveu == 1)
result_df_sobreviventes = result_df[result_df['Sobreviveu'] == 1]

# Contar o total de sobreviventes
total_sobreviventes = result_df_sobreviventes.shape[0]
print(f"Total de pessoas que sobreviveram: {total_sobreviventes}")


# Filtrar para mostrar apenas as pessoas que não sobreviveram (Sobreviveu == 0) com verificação de não nulos
result_df_mortes = result_df[result_df['Sobreviveu'].notnull() & (result_df['Sobreviveu'] == 0)]

# Mostrar as 10 primeiras linhas do DataFrame de mortos
print(result_df_mortes.head(1))

# Contar o total de passageiros
#total_passageiros = X.shape[0]
#print(f"Total de passageiros a bordo: {total_passageiros}")

# Mostrar as 10 últimas linhas do DataFrame
print(result_df.head(10))  # Isso mostrará a estrutura e o número de entradas




