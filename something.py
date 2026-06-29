import pandas as pd
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

# Load input into a dataframe
NBA = pd.read_csv(input())

# Hot encode the game_result variable as a numeric variable with 0 for L and 1 for W
NBA.loc[NBA['game_result']=='L','game_result']=0
NBA.loc[NBA['game_result']=='W','game_result']=1

# Store relevant columns as variables
X = NBA[['pts','elo_i','win_equiv']]
y = NBA[['game_result']].astype(int)

# Scale the input features
scaler = StandardScaler()
XScaled = scaler.fit_transform(X)

np.random.seed(42)

# Split the data into train and test sets
XTrain, XTest, yTrain, yTest = train_test_split(XScaled, y, test_size=0.3, random_state=123)

# Initialize a perceptron model with a learning rate of 0.05 and 20000 epochs
classifyNBA = Perceptron(eta0=0.05, max_iter=20000)
# Fit the perceptron model
classifyNBA.fit(XTrain, yTrain)

# Create a list of predictions from the test features
yPred = classifyNBA.predict(XTest)

# Find the weights for the input variables
weightVar = classifyNBA.coef_
print(weightVar)

# Find the weights for the bias term
weightBias = classifyNBA.intercept_
print(weightBias)

# Find the accuracy score
score = accuracy_score(yTest, yPred)
print('%.3f' % score)