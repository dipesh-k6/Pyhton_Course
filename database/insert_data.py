import sqlite3

conn = sqlite3.connect("student_info.db")
cursor = conn.cursor()


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

    except Exception as e:
        print("Error: ", e)

    else:
        print("\ndata inserted successfully\n")

    finally:
        conn.close()


while True:
    choices = ["insert", "read", "update", "delete", "exit"]
    choice = None

    while choice not in choices:
        choice = input(f"enter your choice from {", ".join(choices)} : ")

    if choice == "insert":
        name = input("enter name : ")
        email = input("enter email : ")
        age = int(input("enter age : "))
        subject = input("enter subject : ")
        fee = int(input("enter fee : "))

        insert_data(name, email, age, subject, fee)
