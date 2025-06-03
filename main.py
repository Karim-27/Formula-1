from src.data_loader import load_session, get_fastest_lap
from src.diagnostics import run_diagnostics
from src.metrics import *
from src.corner_map import slice_corner, find_braking_points
import matplotlib.pyplot as plt
import src.diagnostics

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

session = load_session(2022, "Austria", "Q")
norris_df = get_fastest_lap(session, "NOR")
ricciardo_df = get_fastest_lap(session, "RIC")
nor_braking_zones = find_braking_points(norris_df)
ric_braking_zones = find_braking_points(ricciardo_df)

diagnostic = run_diagnostics(norris_df, ricciardo_df, nor_braking_zones, ric_braking_zones)
print(diagnostic)


# plt.figure(figsize = (12, 6))

# plt.plot(norris_df['Distance'], norris_df['Speed'], label = "Norris Speed")
# plt.plot(ricciardo_df['Distance'], ricciardo_df['Speed'], label = "Ricciardo Speed")
# plt.plot(norris_df['Distance'], norris_df['Brake'].astype(int) * 300, label = 'Norris Brake (scaled)')
# plt.plot(ricciardo_df['Distance'], ricciardo_df['Brake'].astype(int) * 300, label = 'Ricciardo Brake (scaled)', linestyle = '--')
# plt.plot(norris_df['Distance'], norris_df['Throttle'], label = "Norris Throttle")

# plt.plot(norris_df['Brake'].astype(int).values)
# plt.title("Braking vs Index")
# plt.xlabel("Index")
# plt.ylabel("Braking")
#
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()
