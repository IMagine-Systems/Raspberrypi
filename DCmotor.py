from gpiozero import Motor
import time
# 라즈베리파이 GPIO pin 20, 21
motor = Motor(forward=20, backward=21)

while True:
    print('모터 회전 방향 : Forward')
    motor.forward(speed=0.3) # 30% 속도 높이기 speed인자는 1이 100% 0.5는 50%speed.
    time.sleep(5)
    
    print('모터 회전 방향 : Backward')
    motor.backward(speed=0.6) # 60% 속도 줄이기 
    time.sleep(5)