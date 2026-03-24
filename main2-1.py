# gpiozero 라이브러리에서 LED 사용
from gpiozero import LED

# 시간 지연을 위해 sleep 함수 사용
from time import sleep


# 자동차 신호등 LED가 연결된 GPIO 번호
carLedRed = 2
carLedYellow = 3
carLedGreen = 4

# 보행자 신호등 LED가 연결된 GPIO 번호
humanLedRed = 20
humanLedGreen = 21


# GPIO 핀에 LED 객체 생성
carLedRed = LED(2)
carLedYellow = LED(3)
carLedGreen = LED(4)
humanLedRed = LED(20)
humanLedGreen = LED(21)


try:
    # 프로그램이 계속 반복되도록 설정
    while 1:

        # 자동차 초록불 / 보행자 빨간불
        carLedRed.value = 0
        carLedYellow.value = 0
        carLedGreen.value = 1
        humanLedRed.value = 1
        humanLedGreen.value = 0
        sleep(3.0)

        # 자동차 노란불 / 보행자 빨간불
        carLedRed.value = 0
        carLedYellow.value = 1
        carLedGreen.value = 0
        humanLedRed.value = 1
        humanLedGreen.value = 0
        sleep(1.0)

        # 자동차 빨간불 / 보행자 초록불
        carLedRed.value = 1
        carLedYellow.value = 0
        carLedGreen.value = 0
        humanLedRed.value = 0
        humanLedGreen.value = 1
        sleep(3.0)

# 키보드로 프로그램을 중지했을 때
except KeyboardInterrupt:
    pass


# 프로그램 종료 시 LED 모두 끄기
carLedRed.value = 0
carLedYellow.value = 0
carLedGreen.value = 0
humanLedRed.value = 0
humanLedGreen.value = 0

