def weather_calculation(weatherfile):
    minimum_diff = float('inf')
    with open(weatherfile) as weather_file:
        weather = weather_file.readline()
        while weather != "":
            weather = weather_file.readline()
            weather_fields = weather.split()
            if len(weather_fields) > 1:
                try:
                    current_difference = int(weather_fields[1]) - int(weather_fields[2])
                except ValueError:
                    current_difference = int(weather_fields[1].replace("*", "")
                                           [:2]) - int(weather_fields[2].replace("*", "")[:2])
                if current_difference < minimum_diff:
                    minimum_diff = current_difference
                    day = weather_fields[0]
    print(day)

weather_calculation("../weather.dat")
