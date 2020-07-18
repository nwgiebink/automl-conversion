import pandas as pd
from sklearn.model_selection import train_test_split


def label_split(dataframe, train_size):
    X_train, X_test, y_train, y_test = train_test_split(dataframe, dataframe['label'],
                                                        train_size=train_size,
                                                        stratify=dataframe['label'])
    X_train['set'] = 'TRAIN'
    X_test['set'] = 'VALIDATE'
    labeled_df = pd.concat([X_train, X_test])
    return labeled_df