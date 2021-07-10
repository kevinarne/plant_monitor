import matplotlib.pyplot as plt
import sqlmanager

mngr = sqlmanager.MySqlManager("lights")
# pull out weight sensor data
senseData = mngr.execute_mysql("SELECT datetime, val FROM plant_events WHERE code=8 AND plant=2", [])
sensex = [entry[0] for entry in senseData]
sensey = [int(entry[1]) / 100.0 for entry in senseData]

plt.plot(sensex, sensey)
plt.show()
