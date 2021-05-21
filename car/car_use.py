import car
#from car import Car

if __name__ == "__main__":
    my_car = car.Car()
    #my_car = Car()
    my_car.start()
    my_car.accelerate()
    print("speed:", my_car.get_speed())
    my_car.stop()
    print("speed:", my_car.get_speed())

