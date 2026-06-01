import cv2                          # OpenCV 라이브러리
import paho.mqtt.client as mqtt     # MQTT 통신 라이브러리
from gpiozero import LED            # LED 제어 라이브러리

# LED 설정
greenLed = LED(16)   # 녹색 LED (정상 상태)
redLed = LED(21)     # 빨간 LED (졸음 상태)

# MQTT 설정
broker_address = "10.60.3.199"  # MQTT 브로커 IP 주소
client = mqtt.Client()
client.connect(broker_address)

# 웹캠 설정
camera = cv2.VideoCapture(0)        # 웹캠 연결
camera.set(3, 640)                  # 가로 해상도 설정
camera.set(4, 480)                  # 세로 해상도 설정

# 얼굴 및 눈 인식 파일 경로
face_xml = "/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml"
eye_xml = "/usr/share/opencv4/haarcascades/haarcascade_eye.xml"

# 얼굴, 눈 검출 객체 생성
face_cascade = cv2.CascadeClassifier(face_xml)
eye_cascade = cv2.CascadeClassifier(eye_xml)

# 이전 상태 저장 변수
last_state = ""

# 카메라가 켜져 있는 동안 반복
while camera.isOpened():

    # 카메라 영상 읽기
    ret, image = camera.read()

    # 영상 읽기 실패 시 종료
    if not ret:
        print("카메라를 읽지 못했습니다.")
        break

    # 얼굴 인식을 위해 흑백 영상으로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 얼굴 검출
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(100, 100)
    )

    state = "none"  # 현재 상태 초기화

    # 검출된 얼굴마다 반복
    for (x, y, w, h) in faces:

        # 얼굴 영역 사각형 표시
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # 얼굴 부분만 잘라내기
        face_gray = gray[y:y+h, x:x+w]
        face_color = image[y:y+h, x:x+w]

        # 얼굴 내부에서 눈 검출
        eyes = eye_cascade.detectMultiScale(
            face_gray,
            scaleFactor=1.1,
            minNeighbors=5
        )

        # 검출된 눈 표시
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_color,
                          (ex, ey),
                          (ex+ew, ey+eh),
                          (0, 255, 0), 2)

        # 눈이 1개 이하로 검출되면 졸음 상태
        if len(eyes) <= 1:

            state = "drowsy"

            redLed.on()      # 빨간 LED 켜기
            greenLed.off()   # 녹색 LED 끄기

            # 화면에 졸음 상태 표시
            cv2.putText(image,
                        "DROWSY",
                        (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 0, 255),
                        2)

        # 눈이 2개 이상 검출되면 정상 상태
        else:

            state = "awake"

            greenLed.on()    # 녹색 LED 켜기
            redLed.off()     # 빨간 LED 끄기

            # 화면에 정상 상태 표시
            cv2.putText(image,
                        "AWAKE",
                        (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2)

    # 상태가 바뀌었을 때만 MQTT 전송
    if state != "none" and state != last_state:

        client.publish("sleep", state)

        print("MQTT 전송:", state)

        last_state = state

    # 카메라 화면 출력
    cv2.imshow("result", image)

    # q 키 입력 시 종료
    if cv2.waitKey(1) == ord("q"):
        break

# 자원 해제
camera.release()
cv2.destroyAllWindows()

# LED 끄기
greenLed.off()
redLed.off()
