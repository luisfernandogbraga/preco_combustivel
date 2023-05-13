import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


% % writefile gasolina.csv
dia, venda
1, 5.11
2, 4.99
3, 5.02
4, 5.21
5, 5.07
6, 5.09
7, 5.13
8, 5.12
9, 4.94
10, 5.03


df = pd.read_csv('gasolina.csv')

df.head(10)

media = df['venda'].mean()
print(
    f'Média de venda dos 10 primeiros dias de julho de 2021 da gasolina foi : {media} reais.')

sns.set(style='darkgrid')
plt.figure(figsize=(14, 5))
sns.lineplot(data=df, x='dia', y='venda')

plt.title('Preço da gasolina')
plt.xlabel('Dias')
plt.ylabel('Preço de venda')
