import pandas as pd
a=pd.read_csv("C:/Users/AJAY SINGH/OneDrive/Desktop/Top Mentor Data Science/Week-11/train.csv")
#a=pd.read_csv("C:/Users/AJAY SINGH/OneDrive/Desktop/insurance_data.csv")
encoding={'Male':1,'Female':0}
a['Gender']=a['Gender'].map(encoding)
a['Region_Code']=a['Region_Code'].astype(int)
from sklearn.preprocessing import LabelEncoder

le=LabelEncoder()
a['Vehicle_Age']=le.fit_transform(a['Vehicle_Age'])

encoding1={'Yes':1,'No':0}
a['Vehicle_Damage']=a['Vehicle_Damage'].map(encoding1)

a['Policy_Sales_Channel']=a['Policy_Sales_Channel'].astype(int)
a=a.drop('id',axis=1)
'''from sklearn.preprocessing import MinMaxScaler
col=['Gender', 'Age', 'Driving_License', 'Region_Code', 'Previously_Insured',
       'Vehicle_Age', 'Vehicle_Damage', 'Annual_Premium',
       'Policy_Sales_Channel', 'Vintage']
features=a[col]
ss=MinMaxScaler()
a[col]=ss.fit_transform(features)
'''
from sklearn.model_selection import train_test_split
X=a.drop(['Response'],axis=1)
y=a['Response']

## Highly imbalance responses in data
a['Response'].value_counts()
from imblearn.over_sampling import SMOTE
sm=SMOTE(random_state=324)
X_smote,y_smote=sm.fit_resample(X,y)
X_smote1=X_smote.copy()
y_smote1=y_smote.copy()


X_train, X_test, y_train, y_test = train_test_split(X_smote1, y_smote1, test_size=0.20, random_state=1265)
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1265)
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
model_4=RandomForestClassifier()
model_4.fit(X_train,y_train)
y_pred=model_4.predict(X_test)
print(accuracy_score(y_test, y_pred)) 
#print (X_test)
#print(y_test)
#print(y_test==y_pred)
#print(y_smote.loc[])

import pickle
filename = 'insurance.pkl'
pickle.dump(model_4, open(filename, 'wb'))
pickle_file =  pickle.load(open("insurance.pkl", 'rb'))

