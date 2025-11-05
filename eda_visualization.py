import pandas as pd
import matplotli
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6)) #圖表長寬
sns.histplot(df['Sales Volume']) #圖表設定histogram
plt.title('Sales Volume histogram')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
sns.histplot(df['price'])
plt.title('Price histogram')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
sns.boxplot(x='Seasonal', y='Sales Volume', data=df) #箱形圖
plt.title('Box Plot of Sales Volume by Seasonal Category')
plt.show()


