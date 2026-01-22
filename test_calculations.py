import sqlite3
from unittest import TestCase
from calculations import calculate_average_grade_sqlite

class Test(TestCase):
    def test_calculate_average_grade_sqlite(self):
        conn = sqlite3.connect(':memory:')
        conn.execute("CREATE TABLE student_data (grade REAL)")
        conn.execute("INSERT INTO student_data (grade) VALUES (40), (50), (60)")

        result = calculate_average_grade_sqlite(conn)

        # This is right now so it should pass
        self.assertEqual(result, 50)
