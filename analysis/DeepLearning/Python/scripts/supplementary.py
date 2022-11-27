import numpy as np
import pandas as pd
from sklearn.preprocessing import FunctionTransformer

# Encoding Cyclical Features
def cyclical_encoder(df: pd.DataFrame, col: str, period: int, drop: bool = False, inplace: bool = False) -> pd.DataFrame:
    """
    Encode cyclical features as sin and cos components.
    Adapted from https://scikit-learn.org/stable/auto_examples/applications/plot_cyclical_feature_engineering.html
    
    Parameters
    ----------
    df : pd.DataFrame
        The dataframe containing the cyclical feature to be encoded.
    col : str
        The name of the column containing the cyclical feature to be encoded.
    period : int
        The period of the cyclical feature.
    drop : bool, optional
        Whether to drop the original column from the dataframe, by default False
    inplace : bool, optional
        Whether to perform the operation inplace, by default False

    Returns
    -------
    pd.DataFrame
        The dataframe with the cyclical feature encoded.
    """
    
    # Defining transformation functions
    def sin_transformer(period):
        return FunctionTransformer(lambda x: np.sin(x / period * 2 * np.pi))
    def cos_transformer(period):
        return FunctionTransformer(lambda x: np.cos(x / period * 2 * np.pi))
    
    # Creating new columns in the dataframe with the transformed values
    n_df = df.copy()
    n_df.insert(
        loc=list(df.columns).index('hour')+1,
        column = f'{col}_sin',
        value=sin_transformer(period).fit_transform(df[[col]]).values
    )
    n_df.insert(
        loc=list(df.columns).index('hour')+2,
        column = f'{col}_cos',
        value=cos_transformer(period).fit_transform(df[[col]]).values
    )
    if drop:
        n_df.drop(col, axis=1, inplace=True)
    
    if inplace:
        df = n_df
        return None
    else:
        return n_df
