from typing import Dict, Tuple
import pandas as pd

austria_corners = {
    "T1": (50, 200),
    "T3": (270, 350),
    "T4": (520, 600),
    "T6": (680, 760),
    "T7": (765, 800),
    "T8": (820, 900),
    "T9": (970, 1020),
    "T10": (1020, 1080)
}

def get_corner(name:str) -> Tuple[int, int]:
    '''

    '''
    return austria_corners.get(name.upper(), (None, None))

def slice_corner(df: pd.DataFrame, corner: str) -> pd.DataFrame:
    start, end = get_corner(corner)
    if start is None or end is None:
        raise ValueError('start and end are required')
    return df[(df['Distance'] >= start) & (df['Distance'] <= end)]
