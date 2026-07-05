import sqlite3, sys
from datetime import datetime

conn = sqlite3.connect("ticket_parking.db")
cursor = conn.cursor()

#function to insert data
def insert_data(vehicle_num, name, address, vehicle_type):
    try:
        cursor.execute(
            """
                insert into customer_data(vehicle_num, name, address, vehicle_type)
                values (?,?,?,?)
            """,(vehicle_num, name, address, vehicle_type)
        )
        conn.commit()
        print("data inserted successfully\n")

    except Exception as e:
        print("Error inserting data: ",e)
        conn.rollback()


#function to read data
def read_data():
    cursor.execute("select * from customer_data")
    rows = cursor.fetchall()

    if not rows:
        print(" no data to show\n")
    
    else:
        for row in rows:
            print(f"Vehicle_Num: {row[0]} | Name: {row[1]} | Address: {row[2]} | Vehicle_Type: {row[3]} | Entry_Time: {row[4]}")


#funtion to delete data
def del_data(vehicle_num):
    cursor.execute("delete from customer_data where vehicle_num = ?",(vehicle_num,))
    conn.commit()

    if cursor.rowcount>0:
        print(f"{vehicle_num} deleted successfully")
    else:
        print("vehicle with number {vehicle_num} not found")

    
#function to calculate price
def calculate_price(vehicle_num):
    price_info = {2:10, 4:20}
    cursor.execute("select * from customer_data where vehicle_num = ?",(vehicle_num,))
    customer = cursor.fetchone()

    print(type(customer[4]))
    # if customer[3] == 2:
    #     base_price = 10
    #     entry_time = customer[4].timestamp()



while(True):
    valid_choices = ["insert", "read", "update", "delete", "calculate", "exit"]
    choice = None

    while choice not in valid_choices:
        choice = input(f"enter your choice from {", ".join(valid_choices)} : ").strip().lower()

    #inserting data
    if choice == "insert":
        name = input("enter name: ")
        address = input("enter address: ")
        vehicle_num = input("enter vehicle number: ")
        vehicle_type = None
        valid_vehicle_types = ["2", "4"]

        while vehicle_type not in valid_vehicle_types:
            vehicle_type = input("enter 2 for 2wheeler and 4 for 4wheeler: ")

        insert_data(vehicle_num, name, address, vehicle_type)

    #reading data
    if choice == "read":
        read_data()

    #exiting the system
    if choice == "exit":
        conn.close()
        sys.exit(0)

    if choice == "calculate":
        read_data()
        vehicle_num = input("enter vehicle number: ")
        calculate_price(vehicle_num)

    