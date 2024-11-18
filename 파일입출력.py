# 한 줄씩 끝까지 읽기
f = open("C:/doit/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()




# 새로운 파일 쓰기

# 기존 파일 읽기


# 기존 파일에 내용 추가
with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")