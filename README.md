# COMP3005Assignment3
Part 1: Setting up the Database:
1. Create a PostgreSQL database
2. Create the students table in the psql shell or pgAdmin as follows:
    CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE
  );

3. Insert starting data:
    INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');

Part 2: Running the source code:
1. Open a terminal in the directory of the source code file or in an editor.
2. Install the psycopg2 library. Ensure you're in your project directory or virtual environment:
    pip install psycopg2-binary
3. Run the source code file.

Part 3: Youtube Video Link:
https://youtu.be/Ab6sp8KGT00
