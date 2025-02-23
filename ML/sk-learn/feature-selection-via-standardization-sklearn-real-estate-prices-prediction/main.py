### PROJECT ###

# In this project we have a real dataset for real estate prices, size and the year. If you are familiar with the real estate market,
# you can certainly tell that there are almost always a certain causal relationship between these values.
# in this project we will create a multiple linear regression using the attached csv file.

# STEPS we will follow are the following:

#           1. Display the intercept and coefficients.
#           2. Find the R-squared and Adj R-squared.
#           3. Compare the R-squared and Adj R-squared.
#           4. Compare the R-squared of this regression and the simple linear regression where only 'size' was used.
#           5. Using the model make a prediction about an apartment with size 420sq.ft. from 2006.
#           6. Find the univariate p-values of the two variables.
#           7. Create a summary table with the findings.

# Variables:

#           x - price
#           y - size and year

# The most common problem when working with numerical data is the difference in magnitudes.
# An easy for this fix is standardization or aka feature scaling/normalization.

# Standardization is the process of transforming data into a standard scale. The formula used is as per below:

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
data = pd.read_csv('real_estate_price_size_year.csv')

data.head()
data.describe()

## regression model
# // SUPERVISED LEARNING METHOD //

# # ### Declare the dependent & independent variables ###
x = data[['size', 'year']]# this is independent variable or "feature"(input) in sklearn world. This we use to predict the target "y".
y = data['price'] # this is the dependent variable or "target"(output) in sklearn world. This is what we are trying to predict using "x".

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

reg.coef_
# = [67501.57614152, 13724.39708231] - use print() to see the result - they are ordered in the way we fed them.
# but when we get ot the multiple regressions, this array will be filled with the coefficients of each of the features.

# How to find intercept in sklearn #

reg.intercept_
# = 292289.4701599997 - use print() to see the result

# there is difference between R-squared and Adjusted R-squared.
# R-squared - measures the proportion of variance in the dependent(y) variable explain by the independent(x) variables. It always increases when more predictors are added.
# Adj R-squared - adjusts for the number of predictors and decreases if additional variables do NOT contribute to the model's significance.
# Adj R-squared is much more appropriate  measure for multiple linear regression.

# formula for R-squared

# R^2_{adj.} = 1 - (1-R^2)*\frac{n-1}{n-p-1}

# n = 100 (the number of observations/samples)
# p = 2 (the number of predictors)

# How to find the R-squared #

reg.score(x_scaled,y)
# = 0.7764803683276793 - use print() to see the result

# How to find the Adj R-squared #


def adj_r2(x,y):
    r2 = reg.score(x,y) # 1. Given the formula above - first we need to declare a variable R2
    n = x.shape[0] # 2. we find 'n'
    p =x.shape[1]  # 3. we find 'p'
    adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1) # 4. calculate the adj r-squared - R^2_{adj.} ==> 1 - (1-R^2)*\frac{n-1}{n-p-1}
    return adjusted_r2

adj_r2(x_scaled, y)
# = 0.77187171612825

# R-squared      = 0.7764803683276793
# Adj. R-squared = 0.77187171612825

# comparing the above we can conclude that r-squared is larger than the adjusted r-squared i.e. we were NOT being penalized too much for the
# two independent variables ('size' and 'year')

### Create a summary table ###

# Similarly in 'machine learning' context 'intercept' is called 'bias',
# the idea is that the intercept is nothing but a number that adjusts our regression with some constant.
# Then if we need to adjust our regression with some constant, then our regression is 'biased' by that number. So ML world call it 'biased'.

reg_summary = pd.DataFrame([['Bias'], ['size'], ['year']], columns=['Features'])

# 'weights' represent the 'machine learning' word for coefficients.

reg_summary['Weights'] = reg.intercept_, reg.coef_[0], reg.coef_[1]

#       Features    Weights
# 1     Bias        292289.470160
# 2     size        67501.576142
# 3     year        13724.397082

# The greater the 'weight' = the bigger the impact of the feature of the regression. It carries WEIGHT on the result.
# the closer is 'weight' to zero = the smaller its impact.

# using the new naming conventions we can distinguish between a 'regular coefficient summary table'
# and this new one with standardized coefficients (weights).

# When we perform 'feature scaling', we dont care if a useless variable is there or not,
# it will make a little difference if we remove it from the model or leave it there because of the weight of almost zero.
# because zero * zero = zero. This is why sklearn does not natively support p-values
# since most ML practitioners perform some kind of feature scaling before fitting the model -
# we dont really need to identify the worst performing features. They are automatically penalized by having a small weight.

#In general it is preferred to leave out the worst performing features as they interact with useful ones and may BIAS the weight even if its small.


### Making predictions with standardized coefficients (weights). ###

# get new data to use for predictions

new_data = pd.DataFrame(data=[[420,2006], [5000,2024]], columns=['size', 'year'])

reg.predict(new_data)
# = [5.6174092e+07 3.6557835e+08]

# result is confusing - it is an invalid GPA. This is because our regression model was trained
# on standardized inputs. i.e. 'x_scaled' and expects values that are of the same magnitude that we used in the training process.

# when we have a new_date it should be arranged in the same way i.e. 'size', 'year' and also IT MUST BE STANDARDIZED in the same way.

# we already have that stores in our 'scaler' object saved. Lets use the same methodology and create scaled new_data.

new_data_scaled = scaler.transform(new_data) # this scales the new data and standardize it on a similar way. It now looks exactly the same way as the training inputs model.

# finally we can use the predict model on the standardized new_data
reg.predict(new_data_scaled)
# = [ 174438.70685696 1269810.75409429] - the model predicts for examples to have respectively $175K and $1.27M real estate prices.

### Calculate the univariate p-values of the varibles ###

from sklearn.feature_selection import f_regression

f_regression(x_scaled,y)
# = [285.92105192,   0.85525799]), array([8.12763222e-31, 3.57340758e-01]

p_values = f_regression(x,y)[1] # extract p-values from f_regression
# [8.12763222e-31, 3.57340758e-01]

### Create a summary table with findings ###

summary_table = pd.DataFrame(data = x.columns.values, columns=['Features'])
summary_table ['Coefficients'] = reg.coef_
summary_table ['p-values'] = p_values.round(3)

#   Features    Coefficients    p-values
#   size        67501.576142    0.000 (rounded) # --> 'size' p-value meets the requirement to be less than 0.05(its significant)
#   year        13724.397082    0.357 (rounded) # --> 'year' p-value does NOT meet the requirement to be less than 0.05(its significant)

# it seems that 'year' is not event significant, therefore we should remove it from the model.
