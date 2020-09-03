import numpy as np
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression

T = int(input())

for _ in range(T):
    estimator = LinearRegression()
    selector = RFE(estimator, n_features_to_select=1, step=1, verbose=0)

    N = int(input())
    y = np.array(input().split(), float)
    X = np.array([input().split() for _ in range(5)], float)

    selector.fit(X.T, y.T)

    print(np.argmin(selector.ranking_) + 1)
