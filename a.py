import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("C:\\Users\\kumar\\Downloads\\uber.csv")

df.drop(columns=['Drop timestamp'],inplace=True)

df.dropna(inplace=True)

df['Pickup point'].fillna(df['Pickup point'].mode()[0],inplace=True)

k=df.select_dtypes(include="object")
print(k)

c=(df.isnull().sum()/df.shape[0])*100
print(c)

