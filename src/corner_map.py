from typing import Dict, Tuple

import pandas
import pandas as pd
import matplotlib.pyplot as plt

def find_braking_points(df: pandas.DataFrame, min_zone_length = 3):
    '''
    Finds braking zones in the dataframe.
    '''
    if 'Brake' not in df.columns:
        return []

    braking = df['Brake'].astype(int)
    braking_diff = braking.diff().fillna(0)

    start_indices = braking_diff[braking_diff == 1].index
    end_indices = braking_diff[braking_diff == -1].index
    braking_zones = []

    for start in start_indices:
        end_candidates = end_indices[end_indices > start]
        if not end_candidates.empty:
            end = end_candidates[0]

            if end - start >= min_zone_length:
                braking_zones.append((start, end))

    return braking_zones

def get_corner(name:str) -> Tuple[int, int]:
    '''

    '''
    return austria_corners.get(name.upper(), (None, None))

def slice_corner(df: pd.DataFrame, corner: str) -> pd.DataFrame:
    start, end = get_corner(corner)
    if start is None or end is None:
        raise ValueError('start and end are required')
    return df[(df['Distance'] >= start) & (df['Distance'] <= end)]

