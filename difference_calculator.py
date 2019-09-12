from cleaner import Cleaner
'''
module for difference calculation
'''
class DifferenceCalculator(Cleaner):
    '''
    class contains minimum difference head
    and a method to calculate minimum_difference
    '''
    def __init__(self):
        self.minimum_difference = float('inf')
        self.head = ''

    def calculate_difference(self, head_field, field_1, field_2, fields):
        '''
        calculates difference as per given fields
        and stores head with minimum difference
        '''
        if len(fields) > 1:
            try:
                current_difference = abs(int(fields[field_1]) - int(fields[field_2]))
            except ValueError:
                cleaned_field1 = self.get_cleaned_number(fields[field_1])
                cleaned_field2 = self.get_cleaned_number(fields[field_2])
                current_difference = abs(int(cleaned_field1) -
                                         int(cleaned_field2))
            if current_difference < self.minimum_difference:
                self.minimum_difference = current_difference
                self.head = fields[head_field]
