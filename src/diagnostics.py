import pandas as pd
from src.corner_map import slice_corner
from src.metrics import get_braking_point, get_braking_distance, get_min_corner_speed, get_throttle_pickup


def run_diagnostics(driver1_df: pd.DataFrame, driver2_df: pd.DataFrame, d1_braking_zones, d2_braking_zones):
    '''
    Uses all the other functions to compare the driver's fastest laps
    '''
    results = []

    for i in range(min(len(d1_braking_zones), len(d2_braking_zones))):
        d1_corner = slice_corner(driver1_df, d1_braking_zones, i)
        d2_corner = slice_corner(driver2_df, d2_braking_zones, i)

        metrics = {
            "Zone" : i,
            "D1 Brakepoint" : get_braking_point(d1_corner),
            "D2 Brakepoint" : get_braking_point(d2_corner),
            "D1 Brake Distance" : get_braking_distance(d1_corner),
            "D2 Brake Distance" : get_braking_distance(d2_corner),
            "D1 Min Speed" : get_min_corner_speed(d1_corner),
            "D2 Min Speed" : get_min_corner_speed(d2_corner),
            "D1 Throttle Pickup" : get_throttle_pickup(d1_corner),
            "D2 Throttle Pickup" : get_throttle_pickup(d2_corner),
        }

        results.append(metrics)
    return pd.DataFrame(results)


