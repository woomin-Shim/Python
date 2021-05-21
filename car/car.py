class Car:
    def __init__(self):
        self._speed = 0

    def get_speed(self):
        return self._speed

    def start(self):
        print("Engine Start.")
        self._speed = 10

    def accelerate(self):
        print("가속합니다.")
        self._speed += 30

    def stop(self):
        print("정지합니다.")
        self._speed = 0