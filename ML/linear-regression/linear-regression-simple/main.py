import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

# Real estate is one of those examples that every regression course goes through as it is extremely easy to understand
# and there is a (almost always) certain causal relationship to be found.

# You are expected to create a simple linear regression, using the new data.

# In this exercise, the dependent variable is 'price', while the independent variable is 'size'.

### Load Data & Explore###
data = pd.read_csv('real_estate_price_size_year.csv') # real estate data set
data.head()
data.describe()

### Declare the dependent & independent variables ###
y = data['price'] # dependent variable
x1 = data['size'] # independent variable

### Explore dataset in a chart ###
plt.scatter(x1,y)
plt.xlabel('Size',fontsize=20)
plt.ylabel('Price',fontsize=20)
plt.show()

### Regression ###

# formula - Yi = B0 + B1X1

x = sm.add_constant(x1) # add a constant for b0 - always a 1
results = sm.OLS(y,x).fit()
results.summary() # get the coefficient for "Size" and "constant"

### Create the chart ###
plt.scatter(x1,y)
yhat = x1*223.1787+101900 # formula => Yi = B0 + B1X1
fig = plt.plot(x1,yhat, lw=4, c='orange', label ='regression line')
plt.xlabel('Size', fontsize = 20)
plt.ylabel('Price', fontsize = 20)
plt.show()


#Notes:
# [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
# [2] The condition number is large, 2.75e+03. This might indicate that there are
# strong multicollinearity or other numerical problems.


