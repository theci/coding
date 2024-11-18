from datetime import datetime
from unittest import mock

import requests
from constants import STATUS_ENDPOINT
from mock_2 import BuildStatus

# Mocking은 실제 외부 시스템이나 의존성(예: API 호출, 데이터베이스 연결 등)을 대신하여 가짜 객체(mock)를 사용하여 테스트하는 기법입니다. 
# 이를 통해 테스트가 외부 의존성에 영향을 받지 않도록 할 수 있습니다.

# Continuous Integration (CI) 도구와 관련된 머지 리퀘스트(build status) 상태를 처리하는 클래스
class BuildStatus:
    """Continuous Integration 도구에서의 머지 리퀘스트 상태"""

    @staticmethod
    def build_date() -> str: # 현재 시간을 UTC 기준으로 ISO 8601 형식으로 반환하는 정적 메서드
        return datetime.utcnow().isofoormat()

    @classmethod
    def notify(cls, merge_request_id, status): # 머지 리퀘스트 ID와 상태를 API에 전송하는 메서드
        build_status = {
            "id": merge_request_id,
            "status": status,
            "build_at": cls.build_date(), # build_date()를 호출하여 build_at에 현재 시간을 삽입하는데, 이 부분에서 시간에 대한 의존성을 제거하고 테스트하기 위해 mock을 사용합니다
        }
        response = requests.post(STATUS_ENDPOINT, json=build_status) # requests.post()를 사용하여 외부 API에 POST 요청을 보냄
        response.raise_for_status() # 200이 아닐 경우 예외 발생
        return response

# BuildStatus.notify() 메서드가 호출될 때, 실제로 requests.post()가 올바른 URL에 올바른 데이터를 전달하는지 확인하는 테스트입니다. 
# 이를 위해 mock.patch를 사용하여 외부 의존성들을 모킹합니다.
@mock.patch("mock_2.requests") # requests 모듈을 모킹합니다. requests.post() 메서드가 실제로 API를 호출하지 않고 대신 모킹된 객체에서 동작하도록 합니다.
def test_build_notification_sent(mock_requests):
    build_date = "2019-01-01T00:00:01"
    
    # build_date 메서드를 모킹하여 고정된 날짜를 반환하도록 설정
    with mock.patch("mock_2.BuildStatus.build_date", return_value=build_date):
        BuildStatus.notify(123, "OK") # 인자를 받아 API에 POST 요청을 보낸다

    expected_payload = {"id": 123, "status": "OK", "build_at": build_date} # requests.post로 전송될 데이터
    


    # requests.post()가 정확히 STATUS_ENDPOINT에 예상된 페이로드와 함께 호출되었는지를 검증합니다. 만약 requests.post()가 다른 값이나 다른 방식으로 호출되었다면, 테스트가 실패합니다.
    mock_requests.post.assert_called_with(
        STATUS_ENDPOINT, json=expected_payload
    )
