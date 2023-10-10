import sqlite3
import time

# Create the database and table
conn = sqlite3.connect('courses.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS student_scores (
        id INTEGER PRIMARY KEY,
        course_name TEXT,
        student_name TEXT,
        score INTEGER
    )
''')

conn.commit()

# Cache decorator


def cache_decorator(func):
    cache = {}

    def wrapper(*args, **kwargs):
        key = args[0]
        if key in cache:
            start_time = time.time()
            print("Result retrieved from cache.")
            result = cache[key]
            end_time = time.time()
            print(
                f"Time taken from cache: {end_time - start_time:.6f} seconds")
            return result
        else:
            result = func(*args, **kwargs)
            if result is not None:
                cache[key] = result
            return result

    wrapper.cache = cache
    return wrapper

# Timing decorator


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print("Error occurred:", e)
            result = None
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# Add student score to the database


def add_student_score(student_name, score):
    with sqlite3.connect('courses.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO student_scores (course_name, student_name, score)
            VALUES (?, ?, ?)
        ''', ("Python Basics", student_name, score))

# Get student score by ID from the database


@cache_decorator
@timing_decorator
def get_student_score_by_id(student_id):
    with sqlite3.connect('courses.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT course_name, student_name, score FROM student_scores
            WHERE id = ?
        ''', (student_id,))
        result = cursor.fetchone()

        if result:
            return result
        else:
            return None

# Display student data


def display_student_data(student_data):
    if student_data is not None:
        course_name, student_name, student_score = student_data
        print(f"Student: {student_name}")
        print("Course: 'Python Basics'")
        print(f"Score: {student_score}")
        print('-' * 50)
    else:
        print("Student not found.")


# Student data to be added to the database
students_data = [
    ("Guido van Rossum", 100),
    ("Tim Peters", 88),
    ("Raymond Hettinger", 92),
    ("Django Reinhardt", 85),
    ("Flask McConnery", 78),
    ("Pyramid Picasso", 89),
    ("Jake VanderPlas", 95),
    ("Travis Oliphant", 92),
    ("Wes McKinney", 88),
    ("Yoshua Bengio", 90),
    ("Andrew Ng", 92),
    ("Geoffrey Hinton", 95)
]


for student_name, student_score in students_data:
    add_student_score(student_name, student_score)

# Repeated queries
while True:
    print('=' * 50)
    try:
        student_id = int(input("Enter student ID (or -1 to exit): "))
    except ValueError:
        print("Error: Please enter a valid number")
        continue

    if student_id == -1:
        break

    student_data = get_student_score_by_id(student_id)

    print('-' * 50)
    display_student_data(student_data)

    # Display current cache status
    print("Current cache state:")
    CACHE_MIN_ID = 1
    CACHE_MAX_ID = 12
    for key, value in get_student_score_by_id.cache.items():
        if key in range(CACHE_MIN_ID, CACHE_MAX_ID + 1):
            course_name, student_name, student_score = value
            print(
                f"ID: {key}, Course: 'Python Basics', Student: {student_name},"
                f" Score: {student_score}")
    print('=' * 50, end='\n\n')

print("Exiting...")
