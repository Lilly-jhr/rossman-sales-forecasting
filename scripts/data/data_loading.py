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


  