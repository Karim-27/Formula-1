import pandas as pd
import numpy as np


def get_braking_point(df: pd.DataFrame, brake_threshold: float = 10.0):
    '''
    Returns the distance where the driver begins braking
    '''
    braking_data = df[df['Brake']]
    if not braking_data.empty:
        return braking_data['Distance'].iloc[0]
    return None

def get_braking_distance(df: pd.DataFrame, brake_threshold: float = 10.0):
    '''
    Measures the distance where the driver was braking above the threshold
    '''
    braking_data = df[df['Brake']]
    if not braking_data.empty:
        start = braking_data['Distance'].iloc[0]
        end = braking_data['Distance'].iloc[-1]
        return end - start
    return None

def get_min_corner_speed(df: pd.DataFrame, start_dist: float, end_dist: float):
    '''
    Returns the slowest speed of the driver through the corner
    '''
    corner_data = df[(df['Distance'] >= start_dist) & (df['Distance'] <= end_dist)]
    if not corner_data.empty:
        return corner_data['Speed'].min()
    return None

def get_throttle_pickup(df: pd.DataFrame, start_dist: float, end_dist: float, threshold: float = 80.0):
    '''
    Returns the point where the driver's throttle is above 80%
    '''
    corner_exit_data = df[(df['Distance'] >= start_dist) & (df['Distance'] <= end_dist)]
    throttle_data = corner_exit_data[corner_exit_data['Throttle'] >= threshold]
    if not throttle_data.empty:
        return throttle_data['Distance'].iloc[0]
    return None

def get_steering_smoothness(df: pd.DataFrame, start_dist: float, end_dist: float):
    data = df[(df['Distance'] >= start_dist) & (df['Distance'] <= end_dist)]
    return data['Steering Angle'].diff().abs().mean()


