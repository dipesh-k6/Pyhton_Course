import sqlite3
import sys

conn = sqlite3.connect("student_info.db")
cursor = conn.cursor()


# function for data insertion
def insert_data(name, email, age, subject, fee):
    try:
        cursor.execute(
            f"""
            insert into student_info (name, email, age, subject, fee)
            values(
                ?,?,?,?,?
            )
        """,
            (name, email, age, subject, fee),
        )
        conn.commit()
        print("\ndata inserted successfully\n")

    except Exception as e:
        print("Error inserting data: ", e)
        conn.rollback()  # it reverts changes if error occurs

    # else:
    #     print("\ndata inserted successfully\n")

    # finally:
    #     conn.close()


# function to read data
def read_data():
    cursor.execute("select * from student_info")
    rows = cursor.fetchall()

    if not rows:
        print("no data to fetch\n")

    else:
        for data in rows:
            print(f"""
               ID: {data[0]} Name: {data[1]} | Email: {data[2]} | Age: {data[3]} | Subject: {data[4]} | fee: {data[5]}
            """)


# function to delete data
def del_data(student_id):
    cursor.execute("delete from student_info where id= ?", (student_id))
    conn.commit()

    if cursor.rowcount > 0:
        print(f"student with id {student_id} deleted successfully")
    else:
        print(f"student with id {student_id} not found in table")

    # function to update data
    def update_data(id, field, new_value):
        try:
            cursor.execute(
                f"""
                update student_info
                set {field} = ?
                where id = ?
            """,
                (new_value, id),
            )
            print("\ndata updated successfully")

        except Exception as e:
            print("Error updating values : ", e)


while True:
    choices = ["insert", "read", "update", "delete", "exit"]
    choice = None

    while choice not in choices:
        choice = (
            input(f"enter your choice from {", ".join(choices)} : ").strip().lower()
        )

    # exiting the system
    if choice == "exit":
        sys.exit(0)

    # inserting value in table
    if choice == "insert":
        try:  
            name = input("Enter name: ")
            email = input("Enter email: ")
            age = int(input("Enter age: "))
            subject = input("Enter subject: ")
            fee = int(input("Enter fee: "))

        except ValueError as e:
            print("\nPlease enter all numerical values correctly.", e, "\n")

        else:
            insert_data(name, email, age, subject, fee)

    # fetching  data
    if choice == "read":
        read_data()

    # deleteing data
    if choice == "delete":
        read_data()
        student_id = input("enter id of student you want to delete : ")
        del_data(student_id)
