import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.linear_model import LinearRegression


### Load Data & Explore###
data = pd.read_csv('1.01. Simple linear regression - sklearn.csv')

print(data.head())

## regression model
# // SUPERVISED LEARNING METHOD //

# ### Declare the dependent & independent variables ###
x = data['SAT'] # this is independent variable or "feature"(input) in sklearn world. This we use to predict the target "y".
y = data['GPA'] # this is the dependent variable or "target"(output) in sklearn world. This is what we are trying to predict using "x".

### check the shapes of inputs and output ###

x.shape # = (84,) they are both vectors of length 84
y.shape # = (84,) they are both vectors of length 84

# if we were to run this we would get an error that says "Expected 2D array, got 1D array instead".
# Why is this happening? - Our inputs are 1D object and sklearn does not like it. in fact if we go above x.shape = (84, ) line 23/
# x.shape is a vector and thats a single dimension length.

# What we must do? - We must reshape X into a matrix(2D object) as required. We can achieve this by a "reshape" method.
#----------------------------------------------------------------------------------------------#
#x_matrix = x.values.reshape(84,1) # because we only need values from that dataframe.
# By using (84, 1) this way we are not changing anything but the dimensionality. 1D --> 2D.
#----------------------------------------------------------------------------------------------#
# What else can we do? - Use the suggestion from sklearn where it says:
#"Reshape your data either using array.reshape(-1,1) if your data has a single feature or array.reshape(1,-1) if it contains a single sample."

x_matrix = x.values.reshape(-1,1)
x_matrix.shape # = (84, 1)

# we can now proceed feeding them in our algorythm. sklearn takes full advantage of object-oriented capabilities of python such as Classes().
# we need to create an object or an instance of a given class. In this class we will create a "reg"

reg = LinearRegression() # now "reg" is an instance of the LinearRegression class.
# whats now left is to fit the regression.

reg.fit(x_matrix,y) # the order of the items is always first - input; and then target. (x,y). sklearn has different order vs statmodels.
# the result from above is something like
# LinearRegression(copy_x=True, fit_intercept=True, n_jobs=1, NORMALIZE=False)

### STANDARDIZATION: the process of subtracting the mean and dividing by the standard deviation. ###
### NORMALIZATION:  the process of subtracting the mean BUT divide by the L2-norm of the inputs. ###
### COPY_X: when True it copies the inputs before fitting them. This is a safety net againts normalization and other transformations.
### FIT_INTERCEPT: similar to statsmodel.add_constant(x1) this automatically add a constant. If we do not want an intercept, we can change to False
### N-JOBS: is a parameter used when we want to parallelize routines.
# By default only 1(one) CPU is used. If we work on problems with lots of data and have more than 1 CPU, you can change it to 2.3.4.6 CPUs.

# How to find R-squared in sklearn #

reg.score(x_matrix, y) # = 0.40600391479679765

# How to find coefficients in sklearn #

reg.coef_ # the result is an array([0.00165569]) has only one coef
# but when we get ot the multiple regressions, this array will be filled with the coeffcients of each of the features.

# How to find intercept in sklearn #

reg.intercept_ # = 0.2750402996602803 it is a float and not an array because this time a simple linear regression always has a single intercept

# How to make predictions in sklearn #

# how can we predict the GPA using the SAT score. There is a dedicated method called "predict".
# It returns the predictions of the linear regression model for some new inputs.
# predict takes arguments the inputs we want to predict and outputs the prediction according to the model.

reg.predict(1740) # predicts the GPA of a  student with 1740 SAT score

new_data = pd.DataFrame(data=[1740, 1760], columns=['SAT'])

# We can predict the whole data frame in bulk
# Note that the result is an array, this time with 2 elements
reg.predict(new_data)


# Finally, we can directly store the predictions in a new series of the same dataframe
new_data['Predicted_GPA'] = reg.predict(new_data)

# There are different ways to plot the data - here's the matplotlib code
plt.scatter(x,y)

# Parametrized version of the regression line
yhat = reg.coef_*x_matrix + reg.intercept_

# Non-parametrized version of the regression line
#yhat = 0.0017*x + 0.275

# Plotting the regression line
fig = plt.plot(x,yhat, lw=4, c='orange', label ='regression line')

# Labelling our axes
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
plt.show()

