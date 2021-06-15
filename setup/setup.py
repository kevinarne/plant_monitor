import sqlmanager

mngr = sqlmanager.MySqlManager(dbname)
#Create plants table
mngr.create_table("plants", MySqlCol.id_primary(), cols=[MySqlCol("nickname", "VARCHAR(40)"),
    MySqlCol("notes","VARCHAR(200)")])
#Create plant_events table
mngr.create_table("plant_events", MySqlCol.id_primary(), cols = [MySqlCol("code","INT NOT NULL"),
    MySqlCol("datetime","VARCHAR(30)"),
    MySqlCol("val","INT"),
    MySqlCol("plant","INT"),
    MySqlCol("notes","VARCHAR(140)")])
#Create event_codes table
mngr.create_table("event_codes", MySqlCol.id_primary(), cols = [MySqlCol("description","VARCHAR(140)")])
#Create sensors table
mngr.create_table("sensors", MySqlCol.id_primary(), cols = [MySqlCol("description","VARCHAR(140)"),
    MySqlCol("active","VARCHAR(1)"),
    MySqlCol("type","INT"),
    MySqlCol("schedule","VARCHAR(20)"),
    MySqlCol("units","VARCHAR(20)"),
    MySqlCol("subscribed","VARCHAR(30)")])
