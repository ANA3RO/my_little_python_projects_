class Car():
    '''car class(parent)'''
    def __init__(self,car_name,car_model):
        '''Car constructor/initializer'''
        self.car_name = car_name
        self.car_model = car_model
        self.miles = 0
        
    def count_mile(self, mile):
        '''function to count mile of each car instance'''
        self.miles = mile
    
    def description(self):
        '''function to describe each car instance'''
        print('This car is a '+ self.car_name+' '+ self.car_model + ' ' +'with a mileage of '+
        str(self.miles))

    def fill_tank(self):
        '''function to fill up tank of each car instance'''
        print('Tank filled up!')