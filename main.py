'''
main for data munging project
'''
from football import FootballStatistics
from weather import WeatherRepoter
def main():
    '''
    calls weather report and football statistics
    '''
    weather_report = WeatherRepoter('weather.dat')
    weather_report.get_minimum_spread_day()
    football_statistics = FootballStatistics('football.dat')
    football_statistics.get_minimum_goal_difference()
main()
