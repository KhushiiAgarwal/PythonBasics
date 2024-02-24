# -*- coding: utf-8 -*-


from sklearn.datasets import load_boston
import warnings
warnings.filterwarnings('ignore')
boston = load_boston()
#print(boston.data.shape)         # for dataset dimension
#print(boston.feature_names)      # for feature names
#print(boston.target)             # for target variable
#print(boston.DESCR)

import pandas as pd
bos = pd.DataFrame(boston.data, columns = boston.feature_names)
bos['Price'] = boston.target
X = bos.drop("Price", 1)       # feature matrix
y = bos['Price']               # target feature
bos.head()

pip install mlxtend

from mlxtend.feature_selection import SequentialFeatureSelector as sfs
from sklearn.linear_model import LinearRegression


lreg = LinearRegression()
sfs1 = sfs(lreg, k_features=4, forward=True, verbose=2, scoring='neg_mean_squared_error')

sfs1 = sfs1.fit(X, y)

feat_names = list(sfs1.k_feature_names_)
print(feat_names)

new_data = bos[feat_names]
new_data['Price'] = bos['Price']

new_data.head()

new_data.shape, bos.shape


sfs2 = sfs(lreg, k_features=4, forward=False, verbose=1, scoring='neg_mean_squared_error')

sfs2 = sfs2.fit(X, y)

feat_names2 = list(sfs2.k_feature_names_)
print(feat_names2)

new_data2 = bos[feat_names]
new_data2['price'] = bos['Price']

new_data2.head()

