import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
df = pd.DataFrame({'Gender': ['Male','Female','Female','Male'],
                   'Score' : [85,90,78,88],
                   'Branch' : ['ENTC','MECH','CIVIL','CSE'],
                   'CGPA' : [9.13,5.34,9.12,7.24]})

# Plot a boxplot
sns.boxplot(x='Gender', y='Score', data=df)
plt.show()