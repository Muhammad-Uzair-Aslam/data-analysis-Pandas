import pandas as pd
import matplotlib.pyplot as plt
ab=pd.read_csv("air_quality_no2.csv")
ab["usmanghuman"]=ab["station_london"]
print(ab)
ab["usmanghuman"]=(ab["station_london"]/ab["station_antwerp"])
print(ab)