from scipy import stats
import numpy as np
import pandas as pd
import os
from scripts.utils.logger import setup_logger

logger = setup_logger('DataLoader', log_file='logs/data_loading.log')

def load_dataset(file_path):
    """
    Load a dataset from a CSV file.
    """
    logger.info(f"Attempting to load dataset from {file_path}")
    
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        data = pd.read_csv(file_path)
        logger.info(f"Successfully loaded dataset with {data.shape[0]} rows and {data.shape[1]} columns.")
        return data
    except Exception as e:
        logger.error(f"Error loading dataset: {e}")
        raise e




# Z-score method for outlier removal
def remove_outliers_zscore(df, column, threshold=3):
    z_scores = np.abs(stats.zscore(df[column]))
    outliers = z_scores >= threshold
    num_outliers = outliers.sum()
        
    df.drop(df[outliers].index, inplace=True)
        
    logger.info(f"Removed {num_outliers} outliers from {column} using Z-score method.")    
    return df

# Capping method for outlier treatment
def cap_outliers(df, column, lower_quantile=0.01, upper_quantile=0.99): 
    lower_limit = df[column].quantile(lower_quantile)
    upper_limit = df[column].quantile(upper_quantile)
    
    df.loc[df[column] > upper_limit, column] = upper_limit
    df.loc[df[column] < lower_limit, column] = lower_limit
        
    logger.info(f"Capped outliers in {column} between {lower_limit} and {upper_limit}.")
    return df
  