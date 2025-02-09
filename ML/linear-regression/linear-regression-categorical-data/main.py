import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
sns.set()


### Load Data & Explore###
raw_data = pd.read_csv('1.03. Dummies.csv') # dummy data set including a categorical column "attendance" reflecting
                                        # if student attended more than 75% of the lectures.

# mapping of "yes" and "no" values to 1s and 0s with pandas. Dummy => imitation of categories with numbers!

data = raw_data.copy()
data['Attendance'] = data['Attendance'].map({
    'Yes': 1,
    'No': 0
}) #mapping 'Attendance' with new values

print(data.describe()) #the fact that "the mean"  < 0.5(its 0.464286) shows that there are more 0s than 1s
                       # i.e. 46% of students have attended more than 75% of the lessons.
print(data.head())

## regression model


# ### Declare the dependent & independent variables ###
y = data['GPA']
x1 = data[['SAT', 'Attendance']]

### Explore dataset in a chart ###

### x2 ###
y = data['GPA']
x2 = data['SAT']

plt.scatter(x2,y)
plt.xlabel('GPA',fontsize=20)
plt.ylabel('SAT',fontsize=20)
plt.show()

### x3 ###
y = data['GPA']
x3 = data['Attendance']

plt.scatter(x3,y)
plt.xlabel('GPA',fontsize=20)
plt.ylabel('Attendance',fontsize=20)
plt.show()

### Regression ###

# formula - Yi = B0 + B1X1 + B2X2

x = sm.add_constant(x1) # add a constant for b0 - always a 1
results = sm.OLS(y,x).fit()
results.summary() # get the coefficient for "SAT", "Attendance" and "constant"

# Results:
# 1. Our overall model is significant F-statistic = 52.7; Prob(F-statistic) = 2.19e-15
# 2. The SAT score is significant = 0.000; the Attendance(the dummy) score is significant = 0.000
# 3. The Adj.R-squared = 0.555 which is great improvement compared to without the "Attendance"(dummy variable) model result that was = 0.399

#Calculations:
# Before dummy variable ->
# GPA = coef const + coef SAT * SAT
# GPA = 0.275 + 0.0017 * SAT

# With dummy variable   ->
# GPA = coef cons + coef SAT * SAT + coef Attendance(dummy) * Attendance(dummy)
# GPA = 0.6439 + 0.0014 * SAT + 0.2226 * Dummy

### IF STUDENT DID NOT ATTEND ###
# with the dummy - if the student did NOT attend, the dummy would be 0 so ->
# GPA = 0.6439 + 0.0014 * SAT + 0.2226 * 0 ->
# GPA = 0.6439 + 0.0014 * SAT

### IF STUDENT DID ATTEND ###
# with the dummy - if the student did attend, the dummy would be 1 so ->
# GPA = 0.6439 + 0.0014 * SAT + 0.2226 * 1 ->
# GPA = 0.6439 + 0.0014 * SAT + 0.2226 ->
# GPA = 0.8665 + 0.0014 * SAT


plt.scatter(data['SAT'], y)
yhat_no = 0.6439 + 0.0014*data['SAT']  ### IF STUDENT DID NOT ATTEND ###
yhat_yes = 0.8665 + 0.0014*data['SAT'] ### IF STUDENT DID ATTEND ###
fig = plt.plot(data['SAT'], yhat_no, lw=2, c='#006837') # plotting DID NOT ATTEND - NO - 0
fig = plt.plot(data['SAT'], yhat_yes, lw=2, c='#a50026') # plotting DID ATTEND - YES - 1 #a50026
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('SAT', fontsize = 20)
plt.show()

# green regression line --> students did attend
# red regression line --> students did not attend

# overall we have two equations that have the same slope but different intercept
# on average the GPA of those who attended is 0.2226 (dummy coef) higher than students who did NOT attend.


### Coloring the points which refer to students who attended classes versus students who did NOT.(green who did not) ###
plt.scatter(data['SAT'], y, c=data['Attendance'], cmap='RdYlGn_r')
yhat_no = 0.6439 + 0.0014*data['SAT']  ### IF STUDENT DID NOT ATTEND ###
yhat_yes = 0.8665 + 0.0014*data['SAT'] ### IF STUDENT DID ATTEND ###
fig = plt.plot(data['SAT'], yhat_no, lw=2, c='#006837') # plotting DID NOT ATTEND - NO - 0
fig = plt.plot(data['SAT'], yhat_yes, lw=2, c='#a50026') # plotting DID ATTEND - YES - 1 #006837
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('SAT', fontsize = 20)
plt.show()



### adding original regression line ###
plt.scatter(data['SAT'], y, c=data['Attendance'], cmap='RdYlGn_r')
yhat_no = 0.6439 + 0.0014*data['SAT']  ### IF STUDENT DID NOT ATTEND ###
yhat_yes = 0.8665 + 0.0014*data['SAT'] ### IF STUDENT DID ATTEND ###
yhat = 0.0017*data['SAT'] + 0.275
fig = plt.plot(data['SAT'], yhat_no, lw=2, c='#006837', label='regression line1') # plotting DID NOT ATTEND - NO - 0
fig = plt.plot(data['SAT'], yhat_yes, lw=2, c='#a50026', label='regression line2') # plotting DID ATTEND - YES - 1
fig = plt.plot(data['SAT'], yhat, lw=2, c='#4C72B0', label='regression line3') # plotting original regression line
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('SAT', fontsize = 20)
plt.show()

### Conclusion ###
# the original regression line is steeper and it goes somewhat between the two regression lines.
# to use this model for prediction purposes we need an SAT score and Attendance

#### PREDICTION MODEL ####
# lets add new data for two random students John and Angela.
# John has SAT 1700 and did not attend 75% of classes
# Angela has SAT 1670 and did attend 75% of classes

new_data = pd.DataFrame({
    'const': 1, #always 1
    'SAT': [1700, 1670],
    'Attendance': [0,1]
})

new_data = new_data[['const', 'SAT', 'Attendance']] # ordering (optional)
new_data.rename(index={
    0: 'John',
    1: 'Angela'
})

predictions = results.predict(new_data) # the fitted regression for us in the variable: results( results = sm.OLS(y,x).fit()
# 'predict' has a single argument --> new_data
print(predictions)
# the result contains two predictions
# John - 3.023513
# Angela - 3.204163

predictionsdf=pd.DataFrame({'Predictions': predictions})
joined = new_data.join(predictionsdf)
joined.rename(index={0:'John', 1:'Angela'})

#Angela scores lower on the SAT but she attended > 75% of lectures and she is predicted higher GPA than John
# if we use the original regression line without the dummy field, we would predict BOB to have higher GPA than Angela