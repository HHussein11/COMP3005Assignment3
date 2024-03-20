# COMP3005Assignment3
Name: Hamzah Hussein
ID: 101276061

## Part 1: Setting up the Database
Before running the source code, set up your PostgreSQL database.

1. **Create a PostgreSQL database.**

2. **Create the students table.** Use the psql shell or pgAdmin:
    ```sql
    CREATE TABLE students (
        student_id SERIAL PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        enrollment_date DATE
    );
    ```

3. **Insert starting data:**
    ```sql
    INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES
    ('John', 'Doe', 'john.doe@example.com', '2023-09-01'),
    ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),
    ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');
    ```

## Part 2: Running the Source Code
1. **Install psycopg2-binary**: Ensure you're in your project directory or virtual environment.
    ```sh
    pip install psycopg2-binary
    ```
2. **Run the source code file** in a terminal or through your editor.


## Part 3: Youtube Video Link:
https://youtu.be/Ab6sp8KGT00
