import sqlite3

conn = sqlite3.connect("ticket_parking.db")
cursor = conn.cursor()

cursor.execute(
    """
        create table if not exists customer_data(
            vehicle_num varchar(50) primary key,
            name varchar(50) not null,
            address varchar(50) not null,
            vehicle_type int ,
            entry_time timestamp default current_timestamp
        )
    """
)

conn.commit()
conn.close()