import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.linear_model import LinearRegression

# we have a real estate data set in which we will create a simple linear regression using the csv.
# Tasks:
#   1. Create a scatter plot
#   2. Calculate the R-squared
#   3. Display the intercept and coefficients
#   4. Using the model - make a prediction about an apartment with size 750 sq.ft

# The dependent variable(target) is 'price' while the independent variable(feature) is 'size'.

### Load Data & Explore###
data = pd.read_csv('real_estate_price_size (1).csv')

print(data.head())
print(data.describe())

## regression model
# // SUPERVISED LEARNING METHOD //

# ### Declare the dependent & independent variables ###
x = data['size'] # this is independent variable or "feature"(input) in sklearn world. This we use to predict the target "y".
y = data['price'] # this is the dependent variable or "target"(output) in sklearn world. This is what we are trying to predict using "x".

### Explore the data ###

plt.scatter(x,y)
plt.xlabel('Size',fontsize=20)
plt.ylabel('Price',fontsize=20)
plt.show()

### check the shapes of inputs and output ###

x.shape # = (100,) they are both vectors of length 84
y.shape # = (100,) they are both vectors of length 84

# # if we were to run this we would get an error that says "Expected 2D array, got 1D array instead".
# # Why is this happening? - Our inputs are 1D object and sklearn does not like it. in fact if we go above x.shape = (84, ) line 23/
# # x.shape is a vector and thats a single dimension length.
#
# # What we must do? - We must reshape X into a matrix(2D object) as required. We can achieve this by a "reshape" method.
# #----------------------------------------------------------------------------------------------#
# #x_matrix = x.values.reshape(84,1) # because we only need values from that dataframe.
# # By using (84, 1) this way we are not changing anything but the dimensionality. 1D --> 2D.
# #----------------------------------------------------------------------------------------------#
# # What else can we do? - Use the suggestion from sklearn where it says:
# #"Reshape your data either using array.reshape(-1,1) if your data has a single feature or array.reshape(1,-1) if it contains a single sample."
#
x_matrix = x.values.reshape(-1,1)
print(x_matrix.shape) # = (100, 1)
#
# # we can now proceed feeding them in our algorythm. sklearn takes full advantage of object-oriented capabilities of python such as Classes().
# # we need to create an object or an instance of a given class. In this class we will create a "reg"
#
reg = LinearRegression() # now "reg" is an instance of the LinearRegression class.
# # whats now left is to fit the regression.
#
reg.fit(x_matrix,y) # the order of the items is always first - input; and then target. (x,y). sklearn has different order vs statmodels.
# # the result from above is something like
# # LinearRegression(copy_x=True, fit_intercept=True, n_jobs=1, NORMALIZE=False)
#
# ### STANDARDIZATION: the process of subtracting the mean and dividing by the standard deviation. ###
# ### NORMALIZATION:  the process of subtracting the mean BUT divide by the L2-norm of the inputs. ###
# ### COPY_X: when True it copies the inputs before fitting them. This is a safety net againts normalization and other transformations.
# ### FIT_INTERCEPT: similar to statsmodel.add_constant(x1) this automatically add a constant. If we do not want an intercept, we can change to False
# ### N-JOBS: is a parameter used when we want to parallelize routines.
# # By default only 1(one) CPU is used. If we work on problems with lots of data and have more than 1 CPU, you can change it to 2.3.4.6 CPUs.
#
# # How to find R-squared in sklearn #
#
reg.score(x_matrix, y)# = 0.47447391865847587 - use print() to see the result
#
# # How to find coefficients in sklearn #
#
reg.coef_ # the result is an array([223.17874259]) has only one coef - use print() to see the result
# # but when we get ot the multiple regressions, this array will be filled with the coeffcients of each of the features.
#
# # How to find intercept in sklearn #
#
reg.intercept_ # = 101912.60180122912 it is a float and not an array because this time a simple linear regression always has a single intercept - use print() to see the result
#
# # How to make predictions in sklearn #
#
# # how can we predict the 'price' using 'size'? There is a dedicated method called "predict".
# # It returns the predictions of the linear regression model for some new inputs.
# # 'predict' takes arguments the inputs we want to predict and outputs the prediction according to the model.

print(reg.predict([[750]])) # = 269296.65874718 - predicts the 'price' of a real estate with size 750 sq.ft

# NOTE: If your input is a pandas column, then use double brackets ([[]]) get a 2D feature array.

# Why should X be 2D?
# If we look at the source code of fit() (of any model in scikit-learn),
# one of the first things done is to validate the input via the validate_data() method,
# which calls check_array() to validate X. check_array() checks among other things,
# whether X is 2D. It is essential for X to be 2D because ultimately,
# LinearRegression().fit() calls scipy.linalg.lstsq to solve the least squares problem and lstsq requires X to be 2D
# to perform matrix multiplication.
#
# For classifiers, the second dimension is needed to get the number of features, which is essential to get the
# model coefficients in the correct shape.
