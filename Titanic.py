import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\HP\Downloads\titanic dataset.csv")

# therefore we found that we have missing values in our dataset 
#lets perforn EDA on dataset

#Deleting of irrelavent data from dataset.

del df["Name"] #---->name is of no use.
del df["Ticket"] #---->ticket is of no use.
del df["Fare"] #---->fare is of no use.
del df["Cabin"] #---->cabin is of no use.

# changing values for "male","female" string values to numeric values, where male = 1, female = 2.
def getNumber(str):
    if str=="male":
        return 1
    else:
        return 2
    df["Gender"]=df["Sex"].apply(getNumber)
    #also we created column => "Gender" containg numeric values of sex column.
    
#deleting sec column ,coz its of no use now.
del df["Sex"]

# lets handle missing values in "age" column:
meanS = df[df.Survived==1].Age.mean()
meanS    

# creating a new "Age" column 
df["age"]=np.where(pd.isnull(df.Age)& df["Survived"]==1 , meanS,df["Age"])

#finding the mean age of "not survived" people
meaNS=df[df.Survived==0].Age.mean()
meaNS
df.age.fillna(meaNS,inplace=True)

#deleting "Age column as it is of no use now.
del df["Age"]

#lets check whether "Embarked" column is important or not

#finding the number of people who have survived
#given that they have embarked or boarded from a particular port

survivedQ = df[df.Embarked == 'Q'][df.Survived == 1].shape[0]
survivedC = df[df.Embarked == 'C'][df.Survived == 1].shape[0]
survivedS = df[df.Embarked == 'S'][df.Survived == 1].shape[0]
print(survivedQ)
print(survivedC)
print(survivedS)

survivedQ = df[df.Embarked == 'Q'][df.Survived == 0].shape[0]
survivedC = df[df.Embarked == 'C'][df.Survived == 0].shape[0]
survivedS = df[df.Embarked == 'S'][df.Survived == 0].shape[0]
print(survivedQ)
print(survivedC)
print(survivedS)

# conclusion: "Embarked" column is useful but it does contain some missing values 
# removing missing values from the "Embarked" column
df.dropna(inplace=True)

#renaming "age" and "gender" columns
df.rename(columns={'age':'Age'},inplace=True)
df.rename(columns={'Gender':'Sex'},inplace=True)

def getEmb(str):
    if str =="S":
        return 1
    elif str =="Q":
        return 2
    else:
        return 3
df["Embark"]=df["Embarked"].apply(getEmb)

#deleting "Embarked" column as it is of no use
del df['Embarked']
df.rename(columns={'Embark':'Embarked'},inplace= True)

# visualization --->creating a pie chart for number of males and females aboard
from matplotlib import style

males = (df['Sex']==1).sum()
females = (df['Sex']==2).sum()
print(males)
print(females)
    
