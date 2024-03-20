import psycopg2
from psycopg2 import DatabaseError, IntegrityError

# Collects database credentials from the user.
def get_db_credentials():
    dbname = input("Enter database name (default 'a3'): ") or 'a3'
    user = input("Enter username (default 'postgres'): ") or 'postgres'
    password = input("Enter password: ")
    host = input("Enter host (default 'localhost'): ") or 'localhost'
    port = input("Enter port (default '5432'): ") or '5432'
    return {
        'dbname': dbname,  # Database name
        'user': user,  # Username for authentication
        'password': password,  # Password for authentication
        'host': host,  # Database server address
        'port': port  # Port number
    }

# Presents the user with interactive options for database operations.
def interact_with_db(conn):
    while True:  # Keeps showing options until the user chooses to exit.
        print("\nOptions: ")
        # List of operations
        print("1. Get all students")
        print("2. Add a new student")
        print("3. Update student email")
        print("4. Delete a student")
        print("5. Exit")
        choice = input("Select an option: ")  # User selects an operation.

        # Process user's choice and call the respective function
        if choice == '1':
            getAllStudents(conn)
        elif choice == '2':
            # Gather details for the new student
            fname = input("Enter first name: ")
            lname = input("Enter last name: ")
            email = input("Enter email: ")
            edate = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(conn, fname, lname, email, edate)
        elif choice == '3':
            # Update email for a student by ID
            sid = int(input("Enter student id: "))
            email = input("Enter new email: ")
            updateStudentEmail(conn, sid, email)
        elif choice == '4':
            # Delete a student by ID
            sid = int(input("Enter student id to delete: "))
            deleteStudent(conn, sid)
        elif choice == '5':
            break  # Exit the loop and end the program
        else:
            print("Invalid option. Please try again.")

# Retrieves and displays all students from the database.
def getAllStudents(conn):
    try:
        with conn.cursor() as cur:  # Use the connection to create a cursor
            cur.execute("SELECT * FROM students;")
            records = cur.fetchall()  # Fetch all rows of a query result
            for record in records:
                print(record)  # Print each student record
    except (Exception, DatabaseError) as error:
        print(f"Error: {error}")

# Adds a new student record to the database.
def addStudent(conn, first_name, last_name, email, enrollment_date):
    try:
        with conn.cursor() as cur:
            # Insert a new student into the students table
            cur.execute(
                "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
                (first_name, last_name, email, enrollment_date))
            conn.commit()  # Commit the transaction
            print("Student successfully added.")
    except IntegrityError:
        print("Error: This email already exists.")  # Handle duplicate email error
    except (Exception, DatabaseError) as error:
        print(f"Error: {error}")

# Updates an existing student's email.
def updateStudentEmail(conn, student_id, new_email):
    try:
        with conn.cursor() as cur:
            # Update email for a specific student ID
            cur.execute("UPDATE students SET email = %s WHERE student_id = %s;", (new_email, student_id))
            conn.commit()  # Commit the transaction
            print("Email updated successfully.")
    except IntegrityError:
        print("Error: This email already exists.")  # Handle duplicate email error
    except (Exception, DatabaseError) as error:
        print(f"Error: {error}")

# Deletes a student record from the database.
def deleteStudent(conn, student_id):
    try:
        with conn.cursor() as cur:
            # Delete a specific student by ID
            cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
            conn.commit()  # Commit the transaction
            if cur.rowcount:  # Check if the delete operation affected any row
                print(f"Student with id {student_id} deleted successfully.")
            else:
                print(f"Student with id {student_id} does not exist.")
    except (Exception, DatabaseError) as error:
        print(f"Error: {error}")

# Main execution block
if __name__ == "__main__":
    params = get_db_credentials()  # Prompt for credentials at the start
    try:
        conn = psycopg2.connect(**params)  # Establish a database connection
        print("Connected to the database successfully.")
        interact_with_db(conn)  # Enter the interaction loop
    except DatabaseError as e:
        print(f"Failed to connect to the database: {e}")

    # If a connection was established, close it before exiting
    if conn is not None:
        conn.close()