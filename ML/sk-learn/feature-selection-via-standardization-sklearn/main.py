# The most common problem when working with numerical data is the difference in magnitudes.
# An easy for this fix is standardization or aka feature scaling/normalization.

# Standardization is the process of transforming data into a standard scale. The formula used as below:

# z = (x - μ) / σ

# z - standardized variable
# x - original variable
# μ - mean of the data
# σ - standard deviation of data

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.linear_model import LinearRegression

### Load Data & Explore###
data = pd.read_csv('1.02. Multiple linear regression.csv')

print(data.head())
print(data.describe())

## regression model
# // SUPERVISED LEARNING METHOD //

# # ### Declare the dependent & independent variables ###
x = data[['SAT', 'Rand 1,2,3']]# this is independent variable or "feature"(input) in sklearn world. This we use to predict the target "y".
y = data['GPA'] # this is the dependent variable or "target"(output) in sklearn world. This is what we are trying to predict using "x".

### Standardization ###

from sklearn.preprocessing import StandardScaler

# scaler will be used to scale our data i.e. it will subtract the mean(μ) and divide by the std dev (σ) for each point.
scaler = StandardScaler() # we create an empty StandardScaler object. it does not have information in it.

# next step is to fit our input data.
scaler.fit(x) # calculate and stores the mean and std dev for each feature. It will be stored in the 'scaler' object.
# results is something similar like : StandardScaler(copy=True, with_mean=True, with_std=True) --> NOT EMPTY ANYMORE.
# it will contain information about the mean and the std dev.

# in order to apply the scaler we must use another method =>
# 'transform' - it transforms the unscaled inputs using the information contained in the scaler object(feature-wise)
x_scaled = scaler.transform(x) # subtract the mean and divide by std dev for each feature.
print(x_scaled)

# by looking at the coefficients from statsmodel alone we might be deceived.

#       Features    Cofficients     p-values
#          0            SAT           0.000
#          1        Rand 1,2,3        0.676

# Linear Model: SAT * 0.0017 + Rand1,2,3 *(0.0083) + 0.296
#         Jane: 1800*0.0017  +         2 *(0.0083) + 0.296
#         Jane: 3.06         +         -0.0166     + 0.296

# This issue is overcome through feature scaling.

# having all inputs with the same magnitude allows us to compare their impact.

### Regression with scaled features ###

reg = LinearRegression() # now "reg" is an instance of the LinearRegression class.
# whats now left is to fit the regression.

reg.fit(x_scaled,y) # the order of the items is always first - input; and then target. (x_scaled,y). sklearn has different order vs statmodels.
# the result from above is something like
# LinearRegression(copy_x=True, fit_intercept=True, n_jobs=1, NORMALIZE=False)

# # ### STANDARDIZATION: the process of subtracting the mean and dividing by the standard deviation. ###
# # ### NORMALIZATION:  the process of subtracting the mean BUT divide by the L2-norm of the inputs. ###
# # ### COPY_X: when True it copies the inputs before fitting them. This is a safety net againts normalization and other transformations.
# # ### FIT_INTERCEPT: similar to statsmodel.add_constant(x1) this automatically add a constant. If we do not want an intercept, we can change to False
# # ### N-JOBS: is a parameter used when we want to parallelize routines.
# # # By default only 1(one) CPU is used. If we work on problems with lots of data and have more than 1 CPU, you can change it to 2.3.4.6 CPUs.

# How to find coefficients in sklearn #

reg.coef_ # the result is an array([ 0.17181389 -0.00703007]) - use print() to see the result - they are ordered in the way we fed them.
# but when we get ot the multiple regressions, this array will be filled with the coeffcients of each of the features.

# How to find intercept in sklearn #

reg.intercept_ # = 3.330238095238095 - use print() to see the result

### Create a summary table ###

# Similarly in 'machine learning' context 'intercept' is called 'bias',
# the idea is that the intercept is nothing but a number but adjusts our regression with some constant.
# Then if we need to adjust our regression with some constant, then our regression is 'biased' by that number. So ML team call it 'biased'.

reg_summary = pd.DataFrame([['Bias'], ['Sat'], ['Rand 1,2,3']], columns=['Features'])

# 'weights' represent the 'machine learning' word for coefficients.

reg_summary['Weights'] = reg.intercept_, reg.coef_[0], reg.coef_[1]

# The greater the 'weight' = the bigger the impact of the feature of the regression. It carries WEIGHT on the result.
# the closer is 'weight' to zero = the smaller its impact.

# using the new naming conventions we can distinguish between a 'regular coefficient summary table'
# and this new one with standardized coefficients (weights).

# from the result in the summary table we can clearly see that 'Rand 1,2,3' barely contributes to our output.
# When we perform 'feature scaling', we dont care if a useless variable is there or not,
# it will make a little difference if we remove it from the model or leave it there because of the weight of almost zero.
# because zero * zero = zero. This is why sklearn does not natively support p-values
# since most ML practitioners perform some kind of feature scaling before fitting the model -
# we dont really need to identify the worst performing features. They are automatically penalized by having a small weight.

#In general it is preferred to leave out the worst performing features as they interact with useful ones and may BIAS the weight even if its small.


### Making predictions with standardized coefficients (weights). ###

# get new data to use for predictions

new_data = pd.DataFrame(data=[[1700,2], [1800,1]], columns=['SAT', 'Rand 1,2,3'])

reg.predict(new_data)
# result is confusing - it is an invalid GPA. This is because our regression model was trained
# on standardized inputs. i.e. 'x_scaled' and expects values that are of the same magnitude that we used in the training process.

# when we have a new_date it should be arranged in the same way i.e. 'SAT', 'Rand 1,2,3' and also IT MUST BE STANDARDIZED in the same way.

# we already have that stores in our 'scaler' object saved. Lets use the same methodology and create scaled new_data.

new_data_scaled = scaler.transform(new_data) # this scales the new data and standardize it on a similar way. It now looks exactly the same way as the training inputs model.

# finally we can use the predict model on the standardized new_data
reg.predict(new_data_scaled) # = [3.09051403 3.26413803] - the model predicts for examples to have respectively 3.09 and 3.26 GPA scores.


### LETS TRY TO REMOVE THE 'Rand 1,2,3' AS as feature and it doesnt have any weight ### (optional)

reg_simple = LinearRegression()
x_simple_matrix = x_scaled[:,0].reshape(-1,1) # only refer to 'SAT' column, does not include 'Rand 1,2,3' and
# reshape - because sklearn would return error if its out of matrix form
reg_simple.fit(x_simple_matrix,y)

print(reg_simple.predict(new_data_scaled[:,0].reshape(-1,1)))# with argument only feed the 'SAT' score because this regression was trained only on 'SAT' + reshaped.

# results with 'SAT' only  =                   [3.08970998 3.25527879]
# results with 'SAT' and 'Rand 1,2,3' =        [3.09051403 3.26413803]

# this is why sklearn devs decide that p-values are not needed. it doesnt affect the final result because of the weights are close to 0.