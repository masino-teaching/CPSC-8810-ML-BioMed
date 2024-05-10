import numpy as np

def correlation_filter(df, threshold=0.95):
    # Create correlation matrix
    cor_matrix = df.corr().abs()

    # Select upper triangle of correlation matrix
    upper_tri = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))

    # Find index of feature columns with correlation greater than threshold
    to_drop = [column for column in upper_tri.columns if any(upper_tri[column] > threshold)]

    # Drop features
    return to_drop