"""
섭씨온도를 입력받아서 화씨로 변환하기
"""

def fah_converter(celsius):
    return ((9 / 5) * celsius) + 32

print('변환하고 싶은 섭씨 온도를 입력하세요: ')
user_input = input()
fah = fah_converter(float(user_input))
print('섭씨온도 : ', user_input)
print('화씨온도 : {0:.2f}'.format(fah))
print(f'섭씨온도 : {user_input}')
print(f'화씨온도 : {round(fah, 2)}')