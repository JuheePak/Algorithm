from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import validation_curve
import pandas as pd
import numpy as np
from sklearn import tree
import matplotlib.pyplot as plt

"""
max_depth = 최대 깊이
test_size = 테스트 데이터 셋의 비율 혹은 갯수. default = 0.25
min_sample_split = 해당 파라미터 이하의 데이터를 갖고 있는 노드에서는 학습을 멈춤
max_feature = 칼럼중 해당 파라미터만큼만 사용하라
random_state = 데이터 분할 시 셔플할 때 시드값. 수행할 때마다 동일한 결과를 도출하게 함.
train_test_split의 random state는 어떻게 정하느냐에 따라 데이터 세트가 변경될 수 있음.
decisiontreeclassifier의 random state는 동일한 결과 도출 외에도 알고리즘의 초기 weight나 최적의 파라미터를 선택하는 기범에 이를 적용하게 됨.
일반적으로 두 경우 다 random state를 설정하는 것이 좋으나, 최적화를 할 경우 overfitting 될 가능성이 존재함.
shuffle = 셔플여부. default = True
class_weight = 가중치
"""

iris = load_iris()
iris_df = pd.DataFrame(iris.data)
iris_df.columns = iris['feature_names']
iris_df['species'] = iris.target

x_train, x_test, y_train, y_test = train_test_split(iris['data'], iris['target'], test_size=0.2, random_state=11)
clf = tree.DecisionTreeClassifier(max_depth=3, random_state=0)
clf.fit(x_train, y_train)

print(f"score of train dataset : {clf.score(x_train,y_train)}") # 0.975 ?? ovefitting?
print(f"score of test dataset : {clf.score(x_test,y_test)}") # 0.93 too high score

# overfitting이 의심된다. DT는 교차검증 필수!
# 불순도가 높은 것에서 낮은 순서대로 return. 불순도가 낮을 수록 분류가 명확함.

print(clf.feature_importances_) #[0.         0.00862255 0.03311034 0.95826711]
pipe_tree = make_pipeline(tree.DecisionTreeClassifier(criterion="entropy"))
param_range = [2, 3, 4, 5, 6, 7, 8, 9, 10]
train_score, test_score = validation_curve(estimator=pipe_tree,X=x_train,y=y_train,
                param_name = "decisiontreeclassifier__max_depth",
                param_range = param_range, scoring='f1_macro', cv=5, verbose=1)
print(train_score.mean(axis=1))
print(test_score.mean(axis=1))

plt.ylim(0.8,1.2)
plt.plot(param_range, train_score.mean(axis=1),'r--')
plt.plot(param_range, test_score.mean(axis=1),'b--')
plt.show()