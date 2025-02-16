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
data = pd.read_csv('real_estate_price_size_year.csv')

print(data.head())
print(data.describe())

## regression model
# // SUPERVISED LEARNING METHOD //

# # ### Declare the dependent & independent variables ###
x = data[['size', 'year']]# this is independent variable or "feature"(input) in sklearn world. This we use to predict the target "y".
y = data['price'] # this is the dependent variable or "target"(output) in sklearn world. This is what we are trying to predict using "x".

# opposing to simple linear regression, while we are working with multiple linear regressions with sklearn we do not need to reshape the inputs.
# NB: sklearn is optimized to work with multiple linear regressions

# # # we can now proceed feeding them in our algorythm. sklearn takes full advantage of object-oriented capabilities of python such as Classes().
# # # we need to create an object or an instance of a given class. In this class we will create a "reg"

reg = LinearRegression() # now "reg" is an instance of the LinearRegression class.
# whats now left is to fit the regression.

reg.fit(x,y) # the order of the items is always first - input; and then target. (x,y). sklearn has different order vs statmodels.
# the result from above is something like
# LinearRegression(copy_x=True, fit_intercept=True, n_jobs=1, NORMALIZE=False)

# # ### STANDARDIZATION: the process of subtracting the mean and dividing by the standard deviation. ###
# # ### NORMALIZATION:  the process of subtracting the mean BUT divide by the L2-norm of the inputs. ###
# # ### COPY_X: when True it copies the inputs before fitting them. This is a safety net againts normalization and other transformations.
# # ### FIT_INTERCEPT: similar to statsmodel.add_constant(x1) this automatically add a constant. If we do not want an intercept, we can change to False
# # ### N-JOBS: is a parameter used when we want to parallelize routines.
# # # By default only 1(one) CPU is used. If we work on problems with lots of data and have more than 1 CPU, you can change it to 2.3.4.6 CPUs.

# How to find coefficients in sklearn #

reg.coef_ # the result is an array([ 227.70085401 2916.78532684]) has only one coef - use print() to see the result - they are ordered in the way we fed them.
# but when we get ot the multiple regressions, this array will be filled with the coeffcients of each of the features.

# How to find intercept in sklearn #

reg.intercept_ # = -5772267.017463277 - use print() to see the result

# How to find R-squared in sklearn # - one of the common measures of the 'goodness of fit'.
# It is a universal measure to evaluate how well linear regressions perform and compare.

reg.score(x, y) # = 00.7764803683276794 - use print() to see the result

# there is difference between R-squared and Adjusted R-squared.
# R-squared - measures the proportion of variance in the dependent(y) variable explain by the independent(x) variables. It always increases when more predictors are added.
# Adj R-squared - adjusts for the number of predictors and decreases if additional variables do NOT contribute to the model's significance.
# Adj R-squared is much more appropriate  measure for multiple linear regression.

# formula for R-squared

# R^2_{adj.} = 1 - (1-R^2)*\frac{n-1}{n-p-1}

# n = 100 (the number of observations/samples)
# p = 2 (the number of predictors)

x.shape # = (100, 2)

# 1. given the formula above - first we need to declare a variable R2
r2 = reg.score(x, y)

# 2. we find 'n' and 'p'
n = x.shape[0]
p = x.shape[1]

# 3. calculate the adj r-squared - R^2_{adj.} ==> 1 - (1-R^2)*\frac{n-1}{n-p-1}

adj_r2 = 1-(1-r2)*(n-1)/(n-p-1)
adj_r2 # = 0.7718717161282501

# The question is how to detect the variables which are needed in a model?
#
# So the answer is FEATURE SELECTION (F-regression)
# The feature selection simplifies models, improve speed and prevents a series of unwanted issues arising from having too many features.
# In statsmodels summary table, we already have it under P>|t|.
# If a variable has a p-value greater than 0.05, we can disregard it.

# How to find p-values in sklearn?

# feature-selection.f_regression - f-regression created simple linear regressions of each feature and the dependent variable.
# for example with our data it will translate to two regressions:
#               1. size ---> price
#               2. year ---> price
# it will try to predict 'price' with both dependent variables individually. The method will calculate the F-statistics and return the p-values.
# if there were to be 50 features - 50 simple regressions will be created.
# Please note that for a simple linear regression - the p-value of F-stat = the p-value of the only independent variable

### Feature selection ###
from sklearn.feature_selection import f_regression

f_regression(x, y) # = (array([285.92105192,   0.85525799]), array([8.12763222e-31, 3.57340758e-01]))
# there are two arrays:
#       - array([285.92105192,   0.85525799] - contains F-statistics for each of the regressions
#       - array([8.12763222e-31, 3.57340758e-01] - corresponding p-values

# what we need here are only the p-values.

p_values = f_regression(x,y)[1] # = array([8.12763222e-31 3.57340758e-01]
# if numbers are too much see its scientific meaning:
#       e-31 = * 10^-31 / 10^31
#       e-01 = * 10^-1 / 10
# its better to round the numbers for understanding.

p_values.round(3) # [0.   ('size') , 0.357('year')] --> 'size' p-value meets the requirement to be less than 0.05(its significant)

### Creating a summary table

reg_summary = pd.DataFrame(data= x.columns.values, columns=['Features'])
reg_summary['Coefficients'] = reg.coef_
reg_summary['p-values'] = p_values.round(3)

#    Features  Coefficients  p-values
# 0     size   227.700854     0.000
# 1     year   2916.785327    0.357

# the feature 'year' looks insignificant so its better to stick with 'size'

