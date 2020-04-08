# Part 1 - Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('HR.csv')
X = dataset.iloc[:, 0:10].values
y = dataset.iloc[:, 7].values

print(dataset.head())

data = dataset.copy()

print("Data before preprocessing : ")

d = {'satisfaction_level': 0.92, 'last_evaluation': 0.85, 'number_project':  5, 'average_montly_hours' : 259,'time_spend_company': 5 ,'Work_accident':  0, "left" :  1, 'promotion_last_5years' :  0 ,'Departments ':  'sales', 'salary':   'low'}
data = data.append(d, ignore_index=True)

print(data.tail())


# Encoding categorical data
from sklearn.preprocessing import StandardScaler, LabelEncoder
le=LabelEncoder()
for i in data:
    if data[i].dtype == 'object':
        le = LabelEncoder()
        le.fit(data[i].astype(str))
        temp = le.transform(data[i].astype(str))
        if temp.std() == 0:
            print("Dropped attributes with stddev == 0:" , i)
        else:
            one_hot = pd.get_dummies(data[i].astype(str))
            one_hot.columns=[(i+"_"+str(n)) for n in le.classes_]
            one_hot.drop(i +"_"+str(le.classes_[0]),inplace=True,axis=1)
            data = pd.concat([data,one_hot], axis = 1)
            print("Dropped attributes original data after One Hot encoding:", i)
        data.drop([i], inplace = True, axis = 1)

print("Data after preprocessing : ")
print(data.head())

target = ['left']
X = data.drop(target, axis = 1)
y = pd.DataFrame(data[target])

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
print("TEST DATA:",list(X_test[-1]))
# Part 2 - Now let's make the ANN!

# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Dense

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 10, kernel_initializer = 'uniform', activation = 'relu', input_dim = 18))

classifier.add(Dense(units = 10, kernel_initializer = 'uniform', activation = 'relu'))

classifier.add(Dense(units = 6, kernel_initializer = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting the ANN to the Training set
classifier.fit(X_train, y_train, batch_size = 10, epochs = 20)

classifier.save('aml.model')

# Predicting the Test set results

y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

y_test = y_test.astype(bool)

# Making the Confusion Matrix
print("Confusion matrix : ")
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Making the Report
from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))


# new_prediction = classifier.predict(sc.transform(np.array([[0.26,0.7 ,3., 238., 6., 0.,0.,0.,0., 0.,0.,0.,0.,0.,1.,0., 0.,1.]])))
new_prediction = classifier.predict(sc.transform(X[-1:].to_numpy()))
new_prediction = (new_prediction > 0.5)
print(new_prediction)