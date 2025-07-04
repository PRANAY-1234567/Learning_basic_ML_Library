import pandas as pd

# Create a simple DataFrame
data = {
    'Name' : ['Alice','Bob','Charlie','Pranay','Raj'],
    'Age' : [25,30,35,25,26],
    'City' : ['New York','Paris','London','Califiornia','Uganda'],
    'College' : ['COEP','JDIET','YCC','Jh raisoni','Ramdevbaba']
}
df = pd.DataFrame(data)

#Display the DataFrame
print(df)

#Access a coloumn
print(df['Name'])

#Basic Statistics
print(df['Age'].mean()) # Average age

#Filter rows
print(df[df['Age'] > 28])