from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import pandas as pd
import numpy as np
from sklearn import tree

"""
분류트리가 특정 클래스 레이블을 결정하는 것과 달리 회귀 트리는 리프 노드에 속한 데이터 값의 평균값을 구해 회귀 예측값을 계산함
sklearn은 회귀 수행을 할 수 있는 Estimator 클래스를 제공 --> DecisionTreeRegressor
"""
boston = load_boston()
boston_df = pd.DataFrame(boston.data, columns=boston.feature_names) # to dataframe
boston_df['PRICE'] = boston.target
y_target = boston_df['PRICE']
X_data = boston_df.drop(['PRICE'], axis=1, inplace=False)

x_train, x_test, y_train, y_test = train_test_split(X_data, y_target, test_size=0.2, random_state=10)
rm = tree.DecisionTreeRegressor(random_state=3, max_depth=4)
rm.fit(x_train, y_train)

neg_mse_scores = cross_val_score(rm, X_data, y_target, scoring="neg_mean_squared_error", cv = 5)
rmse_scores = np.sqrt(-1 * neg_mse_scores)
avg_rmse = np.mean(rmse_scores)

print(' 5 교차 검증의 개별 Negative MSE scores: ', np.round(neg_mse_scores, 2))
print(' 5 교차 검증의 개별 RMSE scores : ', np.round(rmse_scores, 2))
print(' 5 교차 검증의 평균 RMSE : {0:.3f} '.format(avg_rmse))
