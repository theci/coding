# Fixture는 테스트가 실행되기 전에 필요한 자원(예: 데이터베이스 연결, 파일 생성 등)을 설정하고, 테스트가 끝난 후 정리하는 과정을 의미합니다. 
import sqlite3
import unittest


class TestDatabase(unittest.TestCase):
    def setUp(self):
        # 테스트 전 데이터베이스 연결 설정
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)')

    def tearDown(self):
        # 테스트 후 데이터베이스 정리
        self.conn.close()

    def test_insert_user(self):
        self.cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', ("Alice", "alice@example.com"))
        self.conn.commit()
        self.cursor.execute('SELECT * FROM users')
        user = self.cursor.fetchone()
        self.assertEqual(user[1], "Alice")
        self.assertEqual(user[2], "alice@example.com")

if __name__ == "__main__":
    unittest.main()