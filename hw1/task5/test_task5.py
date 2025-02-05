# test_task5.py

import task5

def test_get_favorite_books():
    books = task5.get_favorite_books()
    assert len(books) >= 5  # Ensure at least 5 books exist
    assert books[0] == ("1984", "George Orwell")  # First book correctness
    assert isinstance(books, list)  # Ensure it is a list

def test_get_first_three_books():
    first_three = task5.get_first_three_books()
    assert len(first_three) == 3  # Ensure only 3 books are returned
    assert first_three == [
        ("1984", "George Orwell"),
        ("Brave New World", "Aldous Huxley"),
        ("To Kill a Mockingbird", "Harper Lee")
    ]  # Ensure the slicing works correctly

def test_get_student_database():
    student_db = task5.get_student_database()
    assert isinstance(student_db, dict)  # Ensure it is a dictionary
    assert "Alice" in student_db  # Ensure a student exists
    assert student_db["Alice"] == 1001  # Ensure correct student ID

def test_get_student_id():
    assert task5.get_student_id("Bob") == 1002  # Check valid student
    assert task5.get_student_id("Eve") == 1005  # Check another valid student
    assert task5.get_student_id("Unknown") is None  # Check non-existent student
