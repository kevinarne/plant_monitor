import matplotlib.pyplot as plt
from matplotlib.dates import date2num, DateFormatter
import datetime as dt
import sqlmanager
import decouple

mngr = sqlmanager.MySqlManager(decouple.config('DB_NAME'))

def filter_zeros(data, tolerance=100):
    return [entry for entry in data if int(entry[1]) > tolerance]

def has_pdt(string):
    if "PDT" in str:
        return True
    return False

if __name__ == "__main__":
    senseData = mngr.execute_mysql("SELECT datetime, val FROM plant_events WHERE code=8 AND plant=2", [])

    senseData = filter_zeros(senseData)

    sensex = [dt.datetime.fromisoformat(entry[0]).timestamp() for entry in senseData]
    sensey = [int(entry[1]) / 100.0 for entry in senseData]

    manualData = mngr.execute_mysql("SELECT datetime, val FROM plant_events WHERE code=2 AND plant=2", [])
    manualx = [dt.datetime.fromisoformat(entry[0]).timestamp() for entry in manualData]
    manualy = [int(entry[1]) / 100.0 for entry in manualData]

    plt.plot(sensex, sensey)
    plt.xlabel("Time")
    plt.ylabel('Weight (oz)')
    plt.plot(manualx, manualy)
    plt.show()
