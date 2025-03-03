mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

# total_missions is the variable for the total mission count
# successful is the variable for the total successful mission count
# percentCal is the variable for the percentage of successful missions
# missionsBefore2000 is the variable for listing of missions before 2000

total_missions= 0
successful= 0

for success in mission_success:
    total_missions += 1
    if success:
        successful += 1

percentCal= (successful/total_missions)*100

missionsBefore2000= [ ]

for m in range(len(mission_names)) : 
    if mission_years[m] < 2000:
        missionsBefore2000.append(mission_names[m])

print('Total number of missions: ' + str(total_missions))
print('Number of successful missions: ' + str(successful))
print(f'Success Rate: {percentCal:.2f}%')
print('Missions launched before the year 2000:')
for mission in missionsBefore2000:
    print(mission)