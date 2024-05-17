def covert_miutes (minutes):
    hours = minutes // 60
    remaning = minutes % 30

    return hours ,remaning

minutes =  int(input())

hours , remaning = covert_miutes(minutes)
print(hours,remaning)