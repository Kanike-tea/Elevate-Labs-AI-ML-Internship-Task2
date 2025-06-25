import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Titanic-Dataset.csv')

#correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix")
plt.show()

# Pairplot for a smaller set of numerical features
selected_cols = ['Age', 'Fare', 'Pclass', 'Survived']
sns.pairplot(df[selected_cols], hue='Survived')
plt.suptitle("Pairplot of Selected Features", y=1.02)
plt.show()
