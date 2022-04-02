import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#loading the dataset to a pandas Dataframe
sonar_data = pd.read_csv('static/sonar data.csv', header=None)
# separating data and Labels
X = sonar_data.drop(columns=60, axis=1)
Y = sonar_data[60]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, stratify=Y, random_state=1)

model = LogisticRegression()
model.fit(X_train, Y_train)
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train) 

#accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test) 

def getData(d):
  
  input_data = (d)

  # changing the input_data to a numpy array
  input_data_as_numpy_array = np.asarray(input_data)

  # reshape the np array as we are predicting for one instance
  input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

  prediction = model.predict(input_data_reshaped)
  print(prediction)

  if (prediction[0]=='R'):
    return 'R'
  else:
    return 'M'