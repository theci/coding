import unittest
from enum import Enum


# 머지 리퀘스트의 상태를 나타내는 Enum 클래스
class MergeRequestStatus(Enum): 
    OPEN = "open"
    APPROVED = "approved"
    REJECTED = "rejected"
    PENDING = "pending"
    CLOSED = "closed"

# 머지 리퀘스트의 상태와 투표 시스템을 관리하는 클래스
class MergeRequest:
    def __init__(self):
        self._context = {
            "upvotes": set(), # 머지 리퀘스트를 찬성하는 유저의 집합
            "downvotes": set(), # 머지 리퀘스트를 반대하는 유저의 집합
        }
        self._status = MergeRequestStatus.OPEN

    def close(self):
        self._status = MergeRequestStatus.CLOSED

    # upvotes와 downvotes를 기준으로 상태를 결정하는 메서드
    @property
    def status(self):
        if self._context["downvotes"]: # 만약 downvotes가 있다면 상태는 REJECTED
            return MergeRequestStatus.REJECTED
        elif len(self._context["upvotes"]) >= 2: # upvotes가 2명 이상이면 상태는 APPROVED
            return MergeRequestStatus.APPROVED
        return MergeRequestStatus.PENDING


    # 머지 리퀘스트가 닫힌 상태일 때는 투표할 수 없도록 _cannot_vote_if_closed() 메서드를 정의
    def _cannot_vote_if_closed(self):
        if self._status == MergeRequestStatus.CLOSED:
            raise Exception("종료된 머지 리퀘스트에 투표할 수 없음")

    def upvote(self, by_user):
        self._cannot_vote_if_closed()
        self._context["downvotes"].discard(by_user)
        self._context["upvotes"].add(by_user)

    def downvote(self, by_user):
        self._cannot_vote_if_closed()
        self._context["upvotes"].discard(by_user)
        self._context["downvotes"].add(by_user)


# merge_request의 upvotes와 downvotes 집합을 바탕으로 머지 리퀘스트의 상태를 결정하는 역할
class AcceptanceThreshold:
    def __init__(self, merge_request: MergeRequest) -> None:
        self._context = merge_request._context

    def status(self):
        if self._context["downvotes"]: # downvotes가 있으면 REJECTED
            return MergeRequestStatus.REJECTED
        elif len(self._context["upvotes"]) >= 2: # upvotes가 2명 이상이면 APPROVED
            return MergeRequestStatus.APPROVED
        return MergeRequestStatus.PENDING




# 테스트할 것들을 파라미터화한 클래스
class TestAcceptanceThreshold(unittest.TestCase):
    def setUp(self): # 테스트에서 사용할 테스트 데이터를 설정하는 메서드
        self.fixture_data = ( #  테스트 케이스마다 검증할 context와 예상되는 expected 상태를 튜플로 묶어서 fixture_data로 저장합니다.
            (
                {"downvotes": set(), "upvotes": set()},
                MergeRequestStatus.PENDING
            ),
            (
                {"downvotes": set(), "upvotes": {"dev1"}},
                MergeRequestStatus.PENDING
            ),
            (
                {"downvotes": {"dev1"}, "upvotes": set()},
                MergeRequestStatus.REJECTED
            ),
            (
                {"downvotes": set(), "upvotes": {"dev1", "dev2"}},
                MergeRequestStatus.APPROVED
            ),
        )

    # 각 context에 대해 AcceptanceThreshold의 status 메서드를 호출하고, 그 결과가 예상한 값과 일치하는지 검증하는 메서드
    def test_status_resolution(self):
        for context, expected in self.fixture_data:
            with self.subTest(context=context):
                merge_request = MergeRequest()
                merge_request._context = context
                status = AcceptanceThreshold(merge_request).status()
                self.assertEqual(status, expected)

if __name__ == "__main__":
    unittest.main()

# 터미널 실행 명령어 : python -m unittest <파일명>.py