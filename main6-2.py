# Raspberry Pi Gas Detection System
# MQ-2 가스 센서를 이용해 가스를 감지하고 부저로 알림을 주는 프로그램

from gpiozero import DigitalInputDevice
from gpiozero import OutputDevice
import time

# 부저와 가스 센서 핀 설정
bz = OutputDevice(18)        # GPIO 18 → 부저
gas = DigitalInputDevice(17) # GPIO 17 → MQ-2 가스 센서

try:
    while True:              # 계속 센서 상태 확인
        if gas.value == 0:   # 가스 감지
            print("가스 감지됨")
            bz.on()          # 부저 켜기
        else:                # 정상 상태
            print("정상")
            bz.off()         # 부저 끄기

        time.sleep(0.2)      # 0.2초마다 반복 확인

except KeyboardInterrupt:    # Ctrl+C 누르면 종료
    pass

bz.off()                     # 종료 시 부저 끄기
