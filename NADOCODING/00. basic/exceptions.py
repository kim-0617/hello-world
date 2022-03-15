class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 전용 나눗셈 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요>>> "))
    num2 = int(input("두번째 숫자를 입력하세요>>> "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("한자리 숫자만 입력하라고 했잖아")
    print(f"{num1}/{num2} = {int(num1/num2)}")
except ValueError:
    print("잘못된 값을 입력하셨습니다.")
except BigNumberError as err:
    print(err)
finally:
    print("계산기를 이용해주셔서 감사합니다.")