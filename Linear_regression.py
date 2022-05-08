import pandas
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
import numpy as np
import pandas as pd


def impact(data) -> pandas.DataFrame:
    """
    This function returns a dataframe with values coefficients sorted by how much
    they impact the target data
    :param data:
    :return:
    """
    X, y = data.data, data.target
    lr = LinearRegression()
    lr.fit(y[:, np.newaxis], X)
    features = pd.DataFrame(index=data.feature_names)
    features['coefficients'] = lr.coef_
    features['impact'] = abs(lr.coef_)

    return features.sort_values('impact', ascending=False)['coefficients']


if __name__ == '__main__':
    dataset = fetch_california_housing()
    print(impact(dataset))

