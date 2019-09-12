def football_calculation(footballfile):
    minimum_diff = float('inf')
    with open(footballfile, 'r') as football:
        football_data = football.readline()
        while football_data != "":
            football_data = football.readline()
            football_fields = football_data.split()
            if len(football_fields) > 1:
                current_difference = abs(int(football_fields[6]) - int(football_fields[8]))
            if current_difference < minimum_diff:
                minimum_diff = current_difference
                team = football_fields[1]
        print(team,'-->',minimum_diff)
football_calculation('../football.dat')
