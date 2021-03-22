import numpy as np
from sklearn.preprocessing import OneHotEncoder

# Two values
sex_enc = OneHotEncoder(
    categories=[np.array(['female','male'])],
    drop='first')
sex_enc.fit(np.array(['female','male']).reshape(-1,1))

# More than two values
embark_enc = OneHotEncoder(
    categories=[np.array(['C','Q','S','UNK'])],
    drop=None)
embark_enc.fit(np.array(['C','Q','S','UNK']).reshape(-1,1))


def preprocess(data):
    '''Convert from a dict to a vector.'''
    # One-hot encoding - Sex
    sex_v = np.array([data['Sex']]).reshape(-1,1)
    # YOUR CODE HERE
    # sex_v = ...

    # One-hot encoding - Embarked
    embark_v = np.array([data['Embarked']]).reshape(-1,1)
    # YOUR CODE HERE
    # embark_v = ...

    # Make sure that the input feature is the same
    # YOUR CODE HERE
    # value = [ ... ]

    return np.array(value)