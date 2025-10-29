import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # using Agg backend for matplotlib
import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')  # if only plt is imported, we switch backend

import seaborn as sns
sns.set(style="whitegrid")
plt.figure(figsize=(8, 6))
sns.histplot(df['Sales Volume'], bins=30, kde=True)
plt.title('Sales Volume histogram')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
sns.histplot(df['price'], bins=30, kde=True)
plt.title('Price histogram')
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 6))
sns.boxplot(x='Seasonal', y='Sales Volume', data=df)
plt.title('Box Plot of Sales Volume by Seasonal Category')
plt.show()

from sklearn.preprocessing import LabelEncoder

cols_to_encode = ['Promotion', 'Seasonal', 'season']
le = LabelEncoder()
for col in cols_to_encode:
    df[col] = le.fit_transform(df[col])

import seaborn as sns
import matplotlib.pyplot as plt

selected_cols = ['Promotion', 'Seasonal', 'Sales Volume', 'price', 'season']
corr_matrix = df[selected_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap of Selected Features")
plt.tight_layout()
plt.show()
