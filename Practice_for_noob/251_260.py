#251
#클래스 : 클래스란 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계도면이다.
#객체 : 객체란 클래스로 만든 피조물을 뜻한다.
#인스턴스 : 인스턴스는 특정 객체가 어떤 클래스의 객체인지를 관계 위주로 설명할 때 사용한다. ex) a는 객체, a는 Cookie의 인스턴스

#252
class Human:
    pass

#253
class Human:
    pass

areum = Human()

#254
class Human:
    def __init__(self):
        print("응애응애")

areum = Human()

#255
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("조아름", 25, "여자")

#256
print(f"이름: {areum.name}, 나이: {areum.age}, 성별: {areum.sex}")

#257
class Human:
    def __init__(self):
        self.name = "모름"
        self.age = 0
        self.sex = "모름"

    def who(self):
        print(f"이름: {self.name}, 나이: {self.age}, 성별: {self.sex}")

#258
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

#259
    def __del__(self):
        print("나의 죽음을 알리지 말라")

#260
class OMG :
    def print(self) :       #self가 빠지면 오류가 발생한다
        print("Oh my god")

mystock = OMG()
mystock.print()