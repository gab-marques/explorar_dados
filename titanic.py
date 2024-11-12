# Carregar o conjunto de dados Titanic
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
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

# Supondo que 'result_df' é o DataFrame que você já criou
# Vamos garantir que temos as colunas 'idade' e 'sexo'
result_df['sexo'] = result_df['Sozinho'].replace({True: 'Masculino', False: 'Feminino'})  # Exemplo de como você pode definir sexo

result_df['sexo'] = result_df['Sozinho'].replace({True: 'Masculino', False: 'Feminino'})  # Exemplo de como você pode definir sexo

# Converter a coluna 'Sobreviveu' para categórica
result_df['Sobreviveu'] = result_df['Sobreviveu'].astype('category')
result_df['Sobreviveu'] = result_df['Sobreviveu'].cat.rename_categories({0: 'Não Sobreviveu', 1: 'Sobreviveu'})

# Criar um gráfico de caixa
plt.figure(figsize=(10, 6))
sns.boxplot(data=result_df, x='sexo', y='Idade', hue='Sobreviveu', palette='coolwarm', dodge=True)
plt.title('Distribuição de Idade por Sexo e Sobrevivência')
plt.xlabel('Sexo')
plt.ylabel('Idade')
plt.legend(title='Sobreviveu', loc='upper right')  # A legenda agora deve mostrar as categorias corretamente
plt.show()
