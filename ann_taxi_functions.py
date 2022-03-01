"""This module contains function and classes required for Taxi Fare Prediction."""

import numpy as np
import pandas as pd

def get_shape(data: pd.DataFrame):
    """This function returns the shape of dataset.

    Args:
        data (pd.DataFrame): The provided dataset. 
        
    Returns:
        The shape of the dataset.
    """
    return data.shape

def get_info(data: pd.DataFrame):
    """This function returns info about dataset.

    Args:
        data (pd.DataFrame): 
        
    Returns:
        Info of the features of the data.
    """
    return data.info()

def null_values(data: pd.DataFrame):
    """Returns number of NULL values in each column.

    Args:
        data (pd.DataFrame): The provided data.

    Returns:
        Number of Null Values in each column.
    """    
    return data.isna().sum()

def read_csv_file(file_name: str):
    """Function for reading a CSV File.

    Args:
        file_name (str): Path or location of file.

    Returns:
        pd.DataFrame: The CSV in the form of Data Frame.
    """
    return pd.read_csv(file_name)

def convert_to_category_type(features: list, data_frame: pd.DataFrame):
    """Function for converting categorical features to category data type.

    Args:
        features (list): List of categorical features. 
        data_frame (pd.DataFrame): DataFrame in which there are categorical features.
        
    Returns:
        pd.DataFrame: The Data Frame with categorical data types.
    """
    for feature in features:
        data_frame[feature] = data_frame[feature].astype('category')
        
def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float):
    """This function calculates distance using Haversine Distance.

    Args:
        lat_1 (float): Source Location Latitude.
        long_1 (float): Source Location Longitude.
        lat_2 (float): Destination Location Latitude.
        long_2 (float): Destination Location Latitude.
        
    Returns:
        float: The distance between two places.
    """
    dLat = np.radians(lat2 - lat1)
    dLon = np.radians(lon2 - lon1)
    lat1 = np.radians(lat1)
    lat2 = np.radians(lat2)
    a = np.sin(dLat / 2)**2 + np.sin(dLon / 2)**2*np.cos(lat1)*np.cos(lat2)
    rad = 6371
    c = 2 * np.arcsin(np.sqrt(a))
    dis = rad * c
    return np.round(dis,2)


def modify_hour(value: str):
    """Function for modifying Hour. 

    Args:
        value (str): Hour Value.

    Returns:
        int: The Interger version of Hour.
    """  
    if value =='00':
        return 0  
    if value.startswith('0'):
        value = value.replace('0', '')
        return int(value)
    else:
        return int(value)
    
def am_or_pm(hour: int):
    """Function for returning AM or PM of the Hour.

    Args:
        hour (int): Hour.
        
    Returns:
        str: The AM or PM of Hour.
    """    
    if hour >= 0 and hour <=12:
        return "AM"
    else:
        return 'PM'
