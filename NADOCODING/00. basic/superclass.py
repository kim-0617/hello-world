class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")
    
        
# class FlyableUnit(Unit, Flyable):
class FlyableUnit(Flyable, Unit): # 순서 변경
    def __init__(self,name):
        # super().__init__()
        Unit.__init__(self) # Unit 클래스 생성자 호출
        Flyable.__init__(self) # Flyable 클래스 생성자 호출
        self.name = name
    def __str__(self):
        return f"{self.name} 뭐라고나올까나?"
    

# 다중상속시에는 super().__init__으로 초기화 해주면 맨첫번째 상속된 클래스만 초기화된다.
# 드랍쉽
dropship = FlyableUnit("이름이요?")
print(dropship)