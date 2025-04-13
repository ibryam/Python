# KMeans Clustering Project

# For this project we will try to use Kmeans Clustering to cluster universities into two groups - Private and Public.

# It is very important to note, we actually have the labels for this dataset, but we will NOT use them for the Kmeans
# clustering algorithm, because it is an unsupervised learning algorithm.

# When using the KMeans algo under normal circumstances, it is because we do not have labels. In this case we will use
# labels to try to get an idea of how well the algo performed., but we wont usually do this for KMeans, so the
# classification report and confusion matrix at the end of this project, do not truly makes sense in the rl setting.

# 1. Import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# 2. Get the data

df = pd.read_csv('College_Data', index_col=0)
df.head()
#                              Private  Apps  ...  Expend  Grad.Rate
# Abilene Christian University     Yes  1660  ...    7041         60
# Adelphi University               Yes  2186  ...   10527         56
# Adrian College                   Yes  1428  ...    8735         54
# Agnes Scott College              Yes   417  ...   19016         59
# Alaska Pacific University        Yes   193  ...   10922         15
#
# [5 rows x 18 columns]

# 3. See details

df.info()
# Index: 777 entries, Abilene Christian University to York College of Pennsylvania
# Data columns (total 18 columns):
#  #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   Private      777 non-null    object
#  1   Apps         777 non-null    int64
#  2   Accept       777 non-null    int64
#  3   Enroll       777 non-null    int64
#  4   Top10perc    777 non-null    int64
#  5   Top25perc    777 non-null    int64
#  6   F.Undergrad  777 non-null    int64
#  7   P.Undergrad  777 non-null    int64
#  8   Outstate     777 non-null    int64
#  9   Room.Board   777 non-null    int64
#  10  Books        777 non-null    int64
#  11  Personal     777 non-null    int64
#  12  PhD          777 non-null    int64
#  13  Terminal     777 non-null    int64
#  14  S.F.Ratio    777 non-null    float64
#  15  perc.alumni  777 non-null    int64
#  16  Expend       777 non-null    int64
#  17  Grad.Rate    777 non-null    int64
# dtypes: float64(1), int64(16), object(1)
# memory usage: 115.3+ KB


df.describe()

#               Apps        Accept  ...        Expend  Grad.Rate
# count    777.000000    777.000000  ...    777.000000  777.00000
# mean    3001.638353   2018.804376  ...   9660.171171   65.46332
# std     3870.201484   2451.113971  ...   5221.768440   17.17771
# min       81.000000     72.000000  ...   3186.000000   10.00000
# 25%      776.000000    604.000000  ...   6751.000000   53.00000
# 50%     1558.000000   1110.000000  ...   8377.000000   65.00000
# 75%     3624.000000   2424.000000  ...  10830.000000   78.00000
# max    48094.000000  26330.000000  ...  56233.000000  118.00000
#
# [8 rows x 17 columns]

# 4. EDA viz
# 4.1 Scatterplot of grad.rate versus room.board - private vs non-private

sns.lmplot(x='Room.Board', y='Grad.Rate', data=df, hue='Private', fit_reg=False,
           palette='coolwarm', height=6, aspect=1)
plt.show()

# 4.2 Scatterplot of F.Undergrad versus Outstate

sns.lmplot(x='Outstate', y='F.Undergrad', data=df, hue='Private', fit_reg=False,
           palette='coolwarm', height=6, aspect=1)
plt.show()

# 4.3 Stacked histogram showing Out of State Tuition based on the Private column.

g = sns.FacetGrid(df, hue='Private', palette='coolwarm', height=6, aspect=2)
g = g.map(plt.hist, 'Outstate', bins=20, alpha=0.7)
g.add_legend()
plt.show()

# 4.4 Stacked histogram showing Grad.Rate on the Private column
sns.set_style('darkgrid')
g = sns.FacetGrid(df,hue="Private",palette='coolwarm',height=6,aspect=2)
g = g.map(plt.hist,'Grad.Rate',bins=20,alpha=0.7)
plt.show()

# 4.4.1 In the results there is a private school with graduation rate higher than 100%. Check what is the name of that school?

df[df['Grad.Rate']>100]
#                   Private  Apps  Accept  ...  perc.alumni  Expend  Grad.Rate
# Cazenovia College     Yes  3847    3433  ...           20    7697        118

# 4.4.2 - Fix the issue to show 118 Grad Rate to 100

df['Grad.Rate']['Cazenovia College'] = 100

# 4.4.3 - Show the updated chart
sns.set_style('darkgrid')
g = sns.FacetGrid(df,hue="Private",palette='coolwarm',height=6,aspect=2)
g = g.map(plt.hist,'Grad.Rate',bins=20,alpha=0.7)
plt.show()

# 5. KMeans Cluster Creation
from sklearn.cluster import KMeans

# 6. Create instance of KMeans model with 2 clusters

kmeans = KMeans(n_clusters=2)

# 7. Fit model to the data

kmeans.fit(df.drop('Private', axis=1))

# 8. What are the cluster center vectors?

kmeans.cluster_centers_


# [[1.00549109e+04 6.73820792e+03 2.74102970e+03 3.29702970e+01
#   6.39009901e+01 1.42840297e+04 2.94107921e+03 8.58346535e+03
#   4.21270297e+03 5.83079208e+02 1.85466337e+03 8.35940594e+01
#   8.90990099e+01 1.61673267e+01 1.62970297e+01 9.95570297e+03
#   6.17623762e+01]
#  [1.94782101e+03 1.31368639e+03 4.86974852e+02 2.67500000e+01
#   5.45857988e+01 2.11855178e+03 5.43665680e+02 1.07181509e+04
#   4.37916420e+03 5.44346154e+02 1.26384320e+03 7.10266272e+01
#   7.82988166e+01 1.37792899e+01 2.37071006e+01 9.61601627e+03
#   6.59896450e+01]]
#
# 9. Evaluation
# There is no perfect way to evaluate clustering if we do not have the labels, however in this dataset we have the luxury of having labels,
# so we can take the advantage of this to evaluate our clusters. Usually having labels wont happen since this is a unsupervised learning model.

# 9.1 Create new column for df called "Cluster", wher 1 is for 'Private" and 0 for "Public".

def converter(private):
    if private == "Yes":
        return 1
    else:
        return 0

df['Cluster'] = df['Private'].apply(converter)

#                              Private  Apps  Accept  ...  Expend  Grad.Rate  Cluster
# Abilene Christian University     Yes  1660    1232  ...    7041         60        1
# Adelphi University               Yes  2186    1924  ...   10527         56        1
# Adrian College                   Yes  1428    1097  ...    8735         54        1
# Agnes Scott College              Yes   417     349  ...   19016         59        1
# Alaska Pacific University        Yes   193     146  ...   10922         15        1

# 10. Create a confusion matrix and classification report to see how well the KMeans clustering worked without being given any labels
from sklearn.metrics import confusion_matrix, classification_report
print(confusion_matrix(df['Cluster'], kmeans.labels_))
print('\n')
print(classification_report(df['Cluster'], kmeans.labels_))

# 10.1 results

# confusion matrix
# [[138  74]
#  [531  34]]

# classification report
#               precision    recall  f1-score   support
#
#            0       0.21      0.65      0.31       212
#            1       0.31      0.06      0.10       565
#
#     accuracy                           0.22       777
#    macro avg       0.26      0.36      0.21       777
# weighted avg       0.29      0.22      0.16       777

# 11. Summary
# Not bad considering the algorithm is purely using the features to cluster the universities into 2 groups.
