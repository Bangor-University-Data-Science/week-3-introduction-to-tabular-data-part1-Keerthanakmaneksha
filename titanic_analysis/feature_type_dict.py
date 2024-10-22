# from titanic_analysis.feature_type_dict import create_feature_type_dict
import pandas as pd
def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': [],  # Fill with continuous numerical features
            'discrete': []  # Fill with discrete numerical features
        },
        'categorical': {
            'nominal': [],  # Fill with nominal categorical features
            'ordinal': []  # Fill with ordinal categorical features
        }
    }

    for  column in df.columns:
        if pd.api.types.is_integer_dtype(df[column]):
            if pd.api.types.is_integer_dtype(df[column]):
                feature_types['numerical']['discrete'].append(column)

            else:
                feature_types['numerical']['continuous'].append(column)
        else:
    
            if df[column].nunique() <= 10:
                feature_types['categorical']['nominal'].append(column)  # Nominal
            else:
                feature_types['categorical']['ordinal'].append(column)  # Ordinal
    return feature_types
