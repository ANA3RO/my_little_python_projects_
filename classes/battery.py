
class Battery():
    '''class for electric car battery'''
    def __init__(self):
        '''battery initializer'''
        self.battery_life = 0
        self.battery_size = 0  

    
    def get_battery_life(self, battery):
        '''function to input battery life'''
        self.battery_life = battery

    def get_battery_size(self, size):
        '''function to input battery size'''
        self.battery_size = size

    def show_battery_life(self):
        '''function to display battery life'''
        print(str(self.battery_life) +' %')


    def show_battery_size(self):
        '''function to display size of battery'''
        print(str(self.battery_size) + ' kwh')