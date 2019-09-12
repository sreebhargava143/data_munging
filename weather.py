'''
contains class that used for weather reports
'''
from difference_calculator import DifferenceCalculator
from extractor import DataExtractor

class WeatherRepoter(DifferenceCalculator, DataExtractor):
    '''
    contains a method that calculates minimum temperature spread
    '''
    def __init__(self, file_path):
        DataExtractor.__init__(self, file_path)
        DifferenceCalculator.__init__(self)
        
    def get_minimum_spread_day(self):
        '''
        calculates the minimum spread of temperature
        '''
        fields = self.get_next_fields()
        while fields != 'EOF':
            self.calculate_difference(0, 1, 2, fields)
            fields = self.get_next_fields()
        print('day:', self.head, '\ntemperature spread:', self.minimum_difference)
