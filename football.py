'''
contains class that is used to calculate statistics
'''
from difference_calculator import DifferenceCalculator
from extractor import DataExtractor

class FootballStatistics(DifferenceCalculator, DataExtractor):
    '''
    contains method to calculate minimum goal difference
    '''
    def __init__(self, file_path):
        DataExtractor.__init__(self, file_path)
        DifferenceCalculator.__init__(self)

    def get_minimum_goal_difference(self):
        '''
        calculates minimum goal difference and stores that team
        with minimum goal difference
        '''
        fields = self.get_next_fields()
        while fields != 'EOF':
            self.calculate_difference(1, 6, 8, fields)
            fields = self.get_next_fields()
        print('team:', self.head, '\nminimum goal difference:', self.minimum_difference)
