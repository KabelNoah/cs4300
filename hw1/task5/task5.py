# task5.py

def get_favorite_books():
    """Returns a list of favorite books (title, author)."""
    return [
        ("1984", "George Orwell"),
        ("Brave New World", "Aldous Huxley"),
        ("To Kill a Mockingbird", "Harper Lee"),
        ("The Catcher in the Rye", "J.D. Salinger"),
        ("The Great Gatsby", "F. Scott Fitzgerald")
    ]

def get_first_three_books():
    """Returns the first three books from the favorite books list using slicing."""
    return get_favorite_books()[:3]

def get_student_database():
    """Returns a dictionary representing a student database."""
    return {
        "Alice": 1001,
        "Bob": 1002,
        "Charlie": 1003,
        "David": 1004,
        "Eve": 1005
    }

def get_student_id(name):
    """Returns the student ID for a given name, or None if not found."""
    student_db = get_student_database()
    return student_db.get(name, None)
