import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
df = pd.DataFrame({
                   'Branch' : ['ENTC','MECH','CIVIL','CSE'],
                   'Score' : [68,85,94,78]})

# Plot a boxplot
sns.boxplot(x='Branch', y='Score', data=df)
plt.show()