from gpiozero import MotionSensor      # PIR 센서 사용
import time                            # 시간 지연
from picamera2 import Picamera2        # 카메라 사용
import datetime                        # 시간 정보 가져오기

pirPin = MotionSensor(16)              # GPIO 16번에 PIR 센서 연결

picam2 = Picamera2()                  # 카메라 객체 생성
camera_config = picam2.create_preview_configuration()  # 기본 설정
picam2.configure(camera_config)       # 설정 적용
picam2.start()                        # 카메라 시작

try:

    while True:                       # 계속 반복 실행
        try:
            sensorValue = pirPin.value   # 센서 값 읽기
            if sensorValue == 1:         # 움직임 감지되면
                now = datetime.datetime.now()   # 현재 시간 저장
                print(now)                     # 시간 출력
                fileName = now.strftime('%y-%m-%d %H-%M-%S')  # 파일 이름 만들기
                picam2.capture_file(fileName + '.jpg')        # 사진 촬영 후 저장
                time.sleep(0.5)         # 너무 많이 찍히지 않게 잠깐 대기

        except:
            pass                        # 오류 나도 계속 실행

except KeyboardInterrupt:
    pass                                # Ctrl+C 누르면 종료



