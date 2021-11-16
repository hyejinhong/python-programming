"""
yesterday.txt 에서 yesterday 가 몇 번 나올까요?

open mode
r : read
w : write
rb : read binary
wb : write binary
a : append
"""
def read_file(file_name):
    with open(file_name, "r", encoding='utf-8') as file:
        lyrics = file.read()
        # print(lyrics)
        return lyrics

lyrics = read_file('../mycode/3_string/yesterday.txt').lower()
print(lyrics)
print(f'yesterday는 {lyrics.count("yesterday")}번 나옵니다.')
