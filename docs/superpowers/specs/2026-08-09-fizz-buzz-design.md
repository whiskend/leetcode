# Fizz Buzz 설계

## 목표

리트코드 Fizz Buzz 문제를 푸는 Python 코드를 추가한다. 1부터 `n`까지 숫자를 문자열 목록으로 반환한다.

## 접근 방법

각 숫자를 15, 3, 5의 배수인지 순서대로 확인한다. 15의 배수를 먼저 처리해야 `FizzBuzz`가 `Fizz` 또는 `Buzz`로 잘못 분리되지 않는다.

시간 복잡도는 O(n)이고, 결과 목록을 제외한 추가 메모리는 O(1)이다.

## 파일

- `python/easy/fizz_buzz.py`: 리트코드 형식의 `Solution.fizzBuzz(n)` 메서드
- `tests/test_fizz_buzz.py`: 숫자, 3의 배수, 5의 배수, 15의 배수 테스트
- `README.md`: 새 쉬운 문제 링크

## 입력 처리

리트코드 조건에 따라 `n`은 양의 정수로 가정한다.

## 검증

`python3 -m unittest discover -s tests -v`로 전체 테스트를 실행한다.
