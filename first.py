def add(n1, n2):
    return n1+n2

print(add(10, 20))

add2 = lambda n1, n2 : n1 + n2
print(add2(10, 15))

# Class 선언
class User:
    # 생성자 선언
    def __init__(self, name):
        self.name = name

    # toString() 오버라이딩
    def __str__(self):
        return "나는 " + self.name + "."

# Class 인스턴스 생성
user = User("파이썬")
print(user)