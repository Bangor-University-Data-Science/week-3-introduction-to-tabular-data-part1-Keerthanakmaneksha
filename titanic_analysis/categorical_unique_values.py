def display_unique_values(df, categorical_features):
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    uniqu_value= {}
    for feature in categorical_features:
        if feature in df:
            uniqu_value[feature] = df[feature].unique()
    # pass  # Implement the logic here
    return uniqu_value
