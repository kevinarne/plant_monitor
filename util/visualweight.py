import matplotlib.pyplot as plt
import datetime as dt
import sqlmanager
import decouple

# These are used as indices, which suggests I should've used a dictionary
DATETIME_IND = 0
VAL_IND = 1

mngr = sqlmanager.MySqlManager(decouple.config('DB_NAME'))

def filter_zeros(data, tolerance=100):
    return [entry for entry in data if int(entry[VAL_IND]) > tolerance]

def filter_extremes(data, cutoff=2000):
    return [entry for entry in data if int(entry[VAL_IND]) < cutoff]

def fix_iso(data):
    new_data = []
    for row in data:
        entry = list(row)
        entry[DATETIME_IND] = dt.datetime.fromisoformat(entry[DATETIME_IND][:19])
        new_data.append(entry)
    return new_data

def adjust_start(data, strt=None, end=None):
    # Start at the beginning of the data and go until the first index after strt
    start_ind = 0
    if strt:
        for _ in range(len(data) - 1):
            if data[start_ind][DATETIME_IND] > strt:
                break
            else:
                start_ind += 1

    # Start at the end and go until the first date that's before end
    end_ind = len(data) - 1
    if end:
        for _ in range(len(data) - 1):
            if data[end_ind][DATETIME_IND] < end:
                break
            else:
                end_ind -= 1
    return data[start_ind : end_ind + 1]

if __name__ == "__main__":
    sense_data = mngr.execute_mysql('SELECT datetime, val FROM plant_events WHERE code=8 AND plant=2', [])

    sense_data = fix_iso(filter_extremes(filter_zeros(sense_data)))

    sensex = [entry[DATETIME_IND] for entry in sense_data]
    sensey = [int(entry[VAL_IND]) / 100.0 for entry in sense_data]

    manual_data = mngr.execute_mysql('SELECT datetime, val FROM plant_events WHERE code=2 AND plant=2', [])

    manual_data = adjust_start(fix_iso(manual_data), strt=sensex[0])

    manualx = [entry[DATETIME_IND] for entry in manual_data]
    manualy = [int(entry[VAL_IND]) / 100.0 for entry in manual_data]

    plt.plot(sensex, sensey)
    plt.xlabel('Time')
    plt.xticks(rotation=30, ha='right')
    plt.ylabel('Weight (oz)')
    plt.plot(manualx, manualy)
    plt.show()
