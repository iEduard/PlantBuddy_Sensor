import psycopg2
from datetime import datetime, timezone

print("Connect")

CONNECTION = "postgres://esc:hKmDeqUNy4yZaJYRz7HFGQA6ns8y6sU@192.168.178.210:5444/homedb"

with psycopg2.connect(CONNECTION) as conn:
    cursor = conn.cursor()
    print(conn.status)
    # use the cursor to interact with your database

    # use the cursor to interact with your database
    cursor.execute("SELECT 'hello world'")
    print(cursor.fetchone())

    sensor_id = 1
    light_intensity = 451.4
    air_temperature = 23.4
    soil_moisture = 50.4
    soil_conductivity = 1102.4
    battery_level = 95.4
    sql_timestamp = datetime.now(timezone.utc)


    sqlStatement = (f"INSERT INTO sensor_data (time, sensor_id, light_intensity, air_temperature,"
                    f"soil_moisture, soil_conductivity, battery_level) VALUES (\'{sql_timestamp}\', {sensor_id}, {light_intensity}," 
                    f"{air_temperature}, {soil_moisture}, {soil_conductivity}, {battery_level});")

    #print(sqlStatement)

    try:
        cursor.execute(sqlStatement)
    except (Exception, psycopg2.Error) as error:
        print(error)
    conn.commit()