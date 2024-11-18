# 단위 테스트 예시: 사용자 이메일 유효성 검사 함수
# 단위테스트 문제점 : 테스트하려는 기능이 다른 부분에 의존하고 있을 때, 그 의존성을 분리하지 않으면 테스트가 어려울 수 있습니다.
import unittest


def is_valid_email(email: str) -> bool:
    # 이메일 형식 체크
    if "@" in email and "." in email:
        return True
    return False

class TestEmailValidator(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(is_valid_email("test@example.com"))

    def test_invalid_email_without_at(self):
        self.assertFalse(is_valid_email("testexample.com"))

    def test_invalid_email_without_dot(self):
        self.assertFalse(is_valid_email("test@examplecom"))

if __name__ == "__main__":
    unittest.main()
    # Ran 3 tests in 0.000s
    # OK


### # 통합 테스트 예시: 사용자 정보 저장 및 조회
# 통합테스트 문제점 : 여러 모듈이 결합되기 때문에 종속성 문제가 발생할 수 있습니다. 데이터베이스나 외부 API와의 연결이 끊길 경우 테스트가 실패할 수 있습니다.

import sqlite3
import unittest


def save_user(name: str, email: str) -> int:
    # 사용자 정보를 DB에 저장
    conn = sqlite3.connect(':memory:')  # 메모리 내 DB 사용
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)')
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    user_id = cursor.lastrowid
    conn.close()
    return user_id

def get_user(user_id: int) -> tuple:
    # 사용자 정보 조회
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

class TestUserFunctions(unittest.TestCase):
    def test_save_and_get_user(self):
        user_id = save_user("Alice", "alice@example.com")
        user = get_user(user_id)
        self.assertEqual(user[1], "Alice")
        self.assertEqual(user[2], "alice@example.com")

if __name__ == "__main__":
    unittest.main()
