import pandas as pd


def get_braking_point(corner_df: pd.DataFrame):
    '''
    Returns the distance where the driver begins braking
    '''
    braking_data = corner_df[corner_df['Brake']]
    if not braking_data.empty:
        return braking_data['Distance'].iloc[0]
    return None

def get_braking_distance(corner_df: pd.DataFrame):
    '''
    Measures the distance where the driver was braking
    '''
    braking_data = corner_df['Brake'].astype(bool).astype(int)
    brake_diff = braking_data.diff().fillna(0)

    start_point = brake_diff[brake_diff == 1].index
    end_point = brake_diff[brake_diff == -1].index

    if start_point.empty or end_point.empty:
        return 0

    start = corner_df.loc[start_point[0], 'Distance']
    valid_end = end_point[end_point > start_point[0]]
    if valid_end.empty:
        return 0

    end = corner_df.loc[end_point[0], 'Distance']
    return end - start

def get_min_corner_speed(corner_df: pd.DataFrame):
    '''
    Returns the slowest speed of the driver through the corner
    '''
    if not corner_df.empty:
        return corner_df['Speed'].min()
    return None

def get_throttle_pickup(corner_df: pd.DataFrame, threshold: float = 50.0):
    '''
    Returns the point where the driver's throttle is above 80% after breaking
    '''
    if corner_df.empty:
        return None

    braking_distance = get_braking_distance(corner_df)
    if braking_distance == 0:
        return None

    brake_series = corner_df['Brake'].astype(int)
    brake_diff = brake_series.diff().fillna(0)
    start_point = brake_diff[brake_diff == 1].index
    end_point = brake_diff[brake_diff == -1].index

    if start_point.empty or end_point.empty:
        return None

    brake_end_point = end_point[end_point > start_point[0]]
    if brake_end_point.empty:
        return None

    throttle_df = corner_df.loc[brake_end_point[0]:]
    throttle_on = throttle_df[throttle_df['Throttle'] > threshold]

    if throttle_on.empty:
        return None

    return throttle_on['Distance'].iloc[0]



