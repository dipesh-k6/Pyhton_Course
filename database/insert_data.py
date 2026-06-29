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

    finally:
        conn.close()

insert_data("adam", "adam@example.com", 29, "python", 25000)