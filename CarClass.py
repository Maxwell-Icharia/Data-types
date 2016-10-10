class Car:

    
    def __init__(self, default_car_name, car_name, default_car_model,
                 car_model, car_properties, car_wheels, car_type, car_speed):
        self.car_name = car_name
        self.car_model = car_model
        self.car_properties = car_properties
        self.car_wheels = car_wheels
        self.car_type = car_type
        self.car_speed = car_speed
        default_car_name = default_car_name
        default_car_model = default_car_model
    
    def name_of_car(self):
        'General' = default_car_name
        if car_name():
            print (default_car_name)
        else:
            print (car_name)

    def model_of_car(self):
