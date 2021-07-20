import decouple
import sqlmanager

mngr = sqlmanager.MySqlManager(decouple.config('DB_NAME'))
vals = mngr.export_table("plant_events")
count = 0

for val in vals:
    if "PDT" in val[2]:
        new_dt = val[2][:10] + val[2][12:]
        query = f"UPDATE plant_events SET datetime = \"{new_dt}\" WHERE id={str(val[0])}"
        mngr.execute_mysql(query,[])
        count += 1

print(count, "rows changed.")
