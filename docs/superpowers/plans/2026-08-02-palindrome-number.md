# Palindrome Number 구현 계획

> **에이전트 작업 규칙:** 이 계획은 작업 단위별로 실행한다. 각 단계는 체크박스로 관리한다.

**목표:** 테스트된 Python Palindrome Number 풀이를 추가하고 원격 `main`에 푸시한다.

**구조:** `Solution.isPalindrome`은 음수를 먼저 제외하고, 나머지 숫자의 자릿수를 뒤집어 원래 값과 비교한다. 테스트는 공개 메서드를 `unittest`로 직접 호출한다.

**기술:** Python 3 표준 라이브러리, `unittest`, Git

## 공통 조건

- 리트코드 `class Solution` 형식을 지킨다.
- 문자열 변환 없이 숫자 연산만 사용한다.
- 시간 복잡도는 O(log n), 추가 메모리는 O(1)이다.
- 외부 라이브러리를 추가하지 않는다.

---

### 작업 1: 테스트와 풀이 추가

**파일:**
- 생성: `python/easy/palindrome_number.py`
- 생성: `tests/test_palindrome_number.py`

**인터페이스:**
- 입력: `x: int`
- 출력: `Solution.isPalindrome(self, x: int) -> bool`

- [ ] **1단계: 실패하는 테스트 작성**

```python
import unittest

from python.easy.palindrome_number import Solution


class PalindromeNumberTests(unittest.TestCase):
    def test_returns_true_for_a_palindrome(self):
        self.assertTrue(Solution().isPalindrome(121))

    def test_returns_false_for_a_non_palindrome(self):
        self.assertFalse(Solution().isPalindrome(10))

    def test_returns_false_for_a_negative_number(self):
        self.assertFalse(Solution().isPalindrome(-121))

    def test_returns_true_for_zero(self):
        self.assertTrue(Solution().isPalindrome(0))
```

- [ ] **2단계: 실패 확인**

실행: `python3 -m unittest discover -s tests -p 'test_palindrome_number.py' -v`

기대: 풀이 모듈이 없어서 실패한다.

- [ ] **3단계: 최소 풀이 작성**

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        reversed_number = 0
        while x > 0:
            reversed_number = reversed_number * 10 + x % 10
            x //= 10

        return original == reversed_number
```

- [ ] **4단계: 테스트 통과 확인**

실행: `python3 -m unittest discover -s tests -v`

기대: 기존 Two Sum 3개와 새 테스트 4개, 총 7개가 통과한다.

### 작업 2: README와 원격 저장소 갱신

**파일:**
- 수정: `README.md`
- 수정: `docs/superpowers/specs/2026-08-02-palindrome-number-design.md`
- 생성: `docs/superpowers/plans/2026-08-02-palindrome-number.md`

**인터페이스:**
- 입력: 새 풀이 파일과 테스트 명령
- 출력: 문제 링크가 있는 README와 원격 `main` 커밋

- [ ] **1단계: README에 문제 링크 추가**

```markdown
- [Palindrome Number](python/easy/palindrome_number.py)
```

- [ ] **2단계: 전체 검증**

실행: `python3 -m unittest discover -s tests -v && git diff --check`

기대: 7개 테스트 통과, 공백 오류 없음.

- [ ] **3단계: 커밋과 푸시**

```bash
git add README.md python/easy/palindrome_number.py tests/test_palindrome_number.py docs/superpowers/specs/2026-08-02-palindrome-number-design.md docs/superpowers/plans/2026-08-02-palindrome-number.md
git commit -m "feat: add palindrome number solution"
git push origin main
```
