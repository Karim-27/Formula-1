from src.data_loader import load_session, get_fastest_lap
from src.metrics import *
from src.corner_map import slice_corner
import matplotlib.pyplot as plt

session = load_session(2022, "Austria", "Q")
norris_df = get_fastest_lap(session, "NOR")
ricciardo_df = get_fastest_lap(session, "RIC")

# norris_T3 = slice_corner(norris_df, "T3")
# ricciardo_T3 = slice_corner(ricciardo_df, "T3")
#
#
# nor_brake_point = get_braking_point(norris_T3)
# print(f"Norris brakes at {nor_brake_point:.2f} m")
# ric_brake_point = get_braking_point(ricciardo_T3)
# print(f"Ricciardo brakes at {ric_brake_point:.2f} m")
#
# nor_brake_distance = get_braking_distance(norris_T3)
# print(f"Norris brakes for {nor_brake_distance:.2f} m")
# ric_brake_distance = get_braking_distance(ricciardo_T3)
# print(f"Ricciardo brakes for {ric_brake_distance:.2f} m")
#
# nor_min_speed = get_min_corner_speed(norris_T3)
# print(f"Norris min speed through T3 is {nor_min_speed:.2f} km/h")
# ric_min_speed = get_min_corner_speed(ricciardo_T3)
# print(f"Ricciardo min speed through T3 is {ric_min_speed:.2f} km/h")
#
# nor_throttle_pickup = get_throttle_pickup(norris_df)
# print(f"Norris throttle picks up above 10% at {nor_throttle_pickup:.2f} m")
# ric_throttle_pickup = get_throttle_pickup(ricciardo_df)
# print(f"Ricciardo throttle picks up above 10% at {ric_throttle_pickup:.2f} m")


plt.figure(figsize = (12, 6))

# plt.plot(norris_df['Distance'], norris_df['Speed'], label = "Norris Speed")
# plt.plot(ricciardo_df['Distance'], ricciardo_df['Speed'], label = "Ricciardo Speed")
# plt.plot(norris_df['Distance'], norris_df['Brake'].astype(int) * 300, label = 'Norris Brake (scaled)')
# plt.plot(ricciardo_df['Distance'], ricciardo_df['Brake'].astype(int) * 300, label = 'Ricciardo Brake (scaled)', linestyle = '--')
# plt.plot(norris_df['Distance'], norris_df['Throttle'], label = "Norris Throttle")

plt.plot(norris_df['Brake'].astype(int).values)
plt.title("Braking vs Index")
plt.xlabel("Index")
plt.ylabel("Braking")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
