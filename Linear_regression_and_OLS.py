
#Implementing a Simple Linear Regression

#Linear Regressions are great for understanding the relationship between a dependent and independent variable.

#Though the basis is simple I have found that it's been helpful in tracking the relationship between spends and revenues when the data is well correlated.

#The input variable or X is the variable that helps predict the value of the output variable Y. 

#A linear regression finds the line that best fits the data

#To find this line we use the Ordinary Least Squares Method(A method for choosing unknown parameters in a linear regression model)

#OLS looks to minimize the sum of the squares of the differences between the observed dependent variable (X) and the output of the function of the independent vairable(y)



#Producting a Random Data Set

np.random.seed(123)
X = []

for i in range(50):
    n = np.random.uniform(1,23)
    X.append(n)
    
y = []

for i in range(50):
    n = np.random.uniform(1,23)
    y.append(n)


# Calculating the OLS for your model

import statsmodels.api as sm


df = pd.DataFrame({'X':X,"y":y})

x = df['X']
y = df['y']

x = sm.add_constant(x)

model = sm.OLS(y,x).fit()
predictions = model.predict(x)

print_model = model.summary()
print(print_model)



# Adjusted R. Squared - Reflects the fit of the model. R-squared values range from 0 to 1. This model has a .06 and so our fit is poor.

#Const. Coefficient - Our Y-intercept. It means that if both the X and Y coefficiecnes are zero the the expected output (ie the Y value) would be equal to the const. coefficient.

#X coefficient - Represents the chanige in the output Y due to a change of one unit of X (X goes up by 1 then y increases by 15.5003)

#STD Error - Reflects the level of accuracy of the coefficients. The lower the value the higher the level of accuracy.

#P>|t| is your p-value. A p-value of less than 0.05 is conssiderded to be statistically signifigant 

#Confidence Interval represents the range in which our coefficients are likely to fall with a 95% confidence.



#importing modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 
from scipy import stats


#Importing scipy stats module so that we can calculate the Slope, Intercept, r, p, and standard error

# r values range from 01 to 1, where 0 meanns no relationship, and 1 (and -1) means 100% related

slope, intercept, r, p, std_error = stats.linregress(X,y)

def linear_regression_plot(X):
    return slope * X + intercept


#The map() iterates through each element of the iterable (in our case, X) and applies the linear_regression_plot function 
model2 = list(map(linear_regression_plot,X))


#Standar matplotlib ploting with no frills
def plot_regression(X,y,model2):
    plt.scatter(X,y)
    plt.plot(X,model2)
    return plt.show()

plot_regression(X,y,model2)

#Predicting the value of Y when X is 20

def plot_prediction(p):
    predicted_value=linear_regression_plot(p)
    print('predicted value: ',p)
    print('relationship: ',r)


    plt.scatter(X,y)
    plt.plot(X,model2)
    plt.axhline(predicted_value,color='orange')
    plt.axvline(20,color='orange')
    return plt.show()

plot_prediction(20)



