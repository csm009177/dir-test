import os
from datetime import datetime 


def nowDate():
    time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    return time
def make_directories(string, count):
    for i in range(count):  
        # 현재 날짜와 시간을 문자열로 가져옴
        now = nowDate()

        # 디렉토리 생성
        os.mkdir(now + "_" + string + str(i))

        # 해당 디렉토리 내에 파일 생성
        with open(now + "_" + string + str(i) + "/" + now + "_" + string + str(i) + ".txt", 'w') as f:
            print(f"{now}_{string}{i}")

# 함수 호출
make_directories("sungmin", 10)

