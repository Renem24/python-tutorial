# super를 사용할 때 문제점
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__() 
        # 2개 이상의 부모 클래스를 다중 상속받으면 맨처음의 클래스만 상속됨.
        # 아래와 같이 각각 선언해줘야 ㄴ함.  
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()