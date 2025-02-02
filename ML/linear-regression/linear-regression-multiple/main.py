import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()

# You are expected to create a multiple linear regression (similar to the one in the lecture), using the new data.

# In this exercise, the dependent variable is 'price', while the independent variables are 'size' and 'year'.

### Load Data & Explore###
data = pd.read_csv('real_estate_price_size_year - multi-year.csv') # real estate data set
data.head()
data.describe()

### Declare the dependent & independent variables ###
y = data['price']
x1 = data[['size', 'year']]

### Explore dataset in a chart ###

### x2 ###
y = data['price']
x2 = data['year']

plt.scatter(x2,y)
plt.xlabel('year',fontsize=20)
plt.ylabel('price',fontsize=20)
plt.show()

### x3 ###
y = data['price']
x3 = data['size']

plt.scatter(x3,y)
plt.xlabel('size',fontsize=20)
plt.ylabel('price',fontsize=20)
plt.show()

### Regression ###

# formula - Yi = B0 + B1X1

x = sm.add_constant(x1) # add a constant for b0 - always a 1
results = sm.OLS(y,x).fit()
results.summary() # get the coefficient for "Size" and "constant"



