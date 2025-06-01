import fastf1

def load_session(year, gp, session):
    session = fastf1.get_session(year, gp, session)
    session.load()
    return session

def get_fastest_lap(session, driver):
    lap = session.laps.pick_drivers(driver).pick_fastest()
    data = lap.get_car_data().add_distance()
    return data

