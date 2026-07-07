import sqlite3, sys, math
from datetime import datetime

conn = sqlite3.connect("ticket_parking.db")
cursor = conn.cursor()


# function to insert data
def insert_data(vehicle_num, name, address, vehicle_type):
    try:
        entry_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #converting to string in iso format
        cursor.execute(
            """
                insert into customer_data(vehicle_num, name, address, vehicle_type, entry_time)
                values (?,?,?,?,?)
            """,
            (vehicle_num, name, address, vehicle_type, entry_time),
        )
        conn.commit()
        print("data inserted successfully\n")

    except Exception as e:
        print("Error inserting data: ", e)
        conn.rollback()


# function to read data
def read_data():
    cursor.execute("select * from customer_data")
    rows = cursor.fetchall()

    if not rows:
        print(" no data to show\n")

    else:
        for row in rows:
            print(
                f"Vehicle_Num: {row[0]} | Name: {row[1]} | Address: {row[2]} | Vehicle_Type: {row[3]} | Entry_Time: {row[4]}"
            )


# funtion to delete data
def del_data(vehicle_num):
    cursor.execute("delete from customer_data where vehicle_num = ?", (vehicle_num,))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"vehicle number {vehicle_num} deleted successfully")
    else:
        print(f"vehicle with number {vehicle_num} not found")


# function to calculate price
def generate_receipt(vehicle_num):
    try:
        price_per_hour = {2: 10, 4: 20}
        cursor.execute("select * from customer_data where vehicle_num = ?", (vehicle_num,))
        customer = cursor.fetchone()

        if not customer:
            print("vehicle not found")
            return
        
        vehicle_type = customer[3]
        entry_time_str = customer[4]
        entry_time = datetime.fromisoformat(entry_time_str)
        exit_time = datetime.now()

        # if timestamp created in and coming from sqlite
            # entry_time_str = customer[4] #sql gives utc time in string
            # entry_time = datetime.strptime(entry_time_str, "%Y-%m-%d %H:%M:%S") #converting to datetime object
            # entry_time = entry_time.replace(tzinfo=timezone.utc) #to tell python its utc
            # exit_time = datetime.now(timezone.utc)

        elapsed_seconds = (exit_time - entry_time).total_seconds()
        elapsed_hours = elapsed_seconds / 3600
        billable_hours = math.ceil(elapsed_hours)

        rate = price_per_hour.get(vehicle_type, 0)
        price = billable_hours * rate
        # print(f"price = rs{price}")

        # creating receipt_file
        filename = f"receipts/receipt_{vehicle_num}.txt"

        with open(filename, "w") as file:
            file.write("=" * 15 + "YOUR BILL=" + "=" * 15)
            file.write(f"\nVehicle Number: {vehicle_num}\n")
            file.write(f"Name: {customer[1]}\n")
            file.write(f"Address: {customer[2]}\n")
            file.write(f"Entry time: {entry_time.strftime("%d/%m/%Y %I:%M:%S %p")}\n")
            file.write(f"Exit time: {exit_time.strftime("%d/%m/%Y %I:%M:%S %p")}\n")
            file.write(f"Vehicle type: {vehicle_type}Wheeler\n")
            file.write("=" * 40 + "\n")
            file.write(f"\nTotal price: Rs {price}\n")

        print(f"receipt generated: {filename}")
        del_data(vehicle_num)
    
    except Exception as e:
        print(f"Error generating receipt: {e}")
        print(f"Record not deleted - try again ")


while True:
    valid_choices = ["insert", "read", "update", "delete", "calculate", "exit"]
    choice = None

    while choice not in valid_choices:
        choice = (
            input(f"enter your choice from {", ".join(valid_choices)} : ")
            .strip()
            .lower()
        )

    # inserting data
    if choice == "insert":
        name = input("enter name: ")
        address = input("enter address: ")
        vehicle_num = input("enter vehicle number: ")
        vehicle_type = None
        valid_vehicle_types = ["2", "4"]

        while vehicle_type not in valid_vehicle_types:
            vehicle_type = input("enter 2 for 2wheeler and 4 for 4wheeler: ")

        insert_data(vehicle_num, name, address, vehicle_type)

    # reading data
    if choice == "read":
        read_data()

    # exiting the system
    if choice == "exit":
        conn.close()
        sys.exit(0)

    if choice == "calculate":
        read_data()
        vehicle_num = input("enter vehicle number: ")
        generate_receipt(vehicle_num)
