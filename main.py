import pandas as pd
import numpy as np

plane = pd.read_excel('AirplaneData.xlsx')

plane["Total Seats"] = plane["Business Seats"] + plane["Economy Seats"]
print(plane.head())
