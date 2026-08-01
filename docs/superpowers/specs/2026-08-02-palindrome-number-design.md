# Palindrome Number 설계

## 목표

리트코드 Palindrome Number 문제를 푸는 Python 코드를 추가한다. 정수를 앞뒤로 읽었을 때 같은 숫자인지 반환한다.

## 접근 방법

문자열로 바꾸지 않고 숫자 연산으로 처리한다. 음수는 `False`를 반환하고, 0 이상 숫자는 자릿수를 뒤집은 값과 원래 값을 비교한다.

자릿수가 `log n`개일 때 시간은 O(log n), 추가 메모리는 O(1)이다.

## 파일

- `python/easy/palindrome_number.py`: 리트코드 형식의 `Solution.isPalindrome(x)` 메서드
- `tests/test_palindrome_number.py`: 팰린드롬, 일반 숫자, 음수, 0 테스트
- `README.md`: 새 쉬운 문제 링크

## 입력 처리

리트코드는 정수만 전달하므로 별도 형 변환이나 검증은 하지 않는다. 모든 입력 정수에 대해 불리언 값을 반환한다.

## 검증

`python3 -m unittest discover -s tests -v`로 전체 테스트를 실행한다.
