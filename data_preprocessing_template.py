import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#creating dataframes
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,3].values

# MISSING DATA

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = "mean",axis=0)
X[:,1:3] = imputer.fit_transform(X[:,1:3])

# encode categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
label = LabelEncoder()
X[:,0] = label.fit_transform(X[:,0])
oneHotEncoder = OneHotEncoder(categorical_features = [0])
X = oneHotEncoder.fit_transform(X).toarray()
Y = label.fit_transform(Y)

#splitting the data
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

# feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test =sc_X.transform(X_test) 