from classes.my_car import Car
from classes.battery import Battery

class Electric_Car(Car, Battery):
    def __init__(self, car_name, car_model):
        '''initializer with inherited initialized variables from car'''
        super().__init__(car_name, car_model)
        

    def description(self):
        '''description of electric car'''
        print('This car is a '+ self.car_name.title() +' '+ self.car_model.title() +' ' + 'with a mileage of '+
        str(self.miles) + ' ' + 'miles a battery life of ' + str(self.battery_life) + ' % and a battery size of ' +
        str(self.battery_size) + ' kwh')

    def fill_tank(self):
        print('This is an Electric car!')