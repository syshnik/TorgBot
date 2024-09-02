import ephem
 
 # Фаза Луны возвращается в виде дроби,
 #  где 0,0 — новолуние, 0,25 — первая четверть, 0,5 — полнолуние, 0,75 — последняя четверть, а 1,0 — снова новолуние.
 
def GetMoonPhase():
    # Define the observer's location
    observer = ephem.Observer()
    observer.lat = '54.7261409'
    observer.long = '55.947499'
    
    # Define the date
    observer.date = '2023/02/03'
    
    # Define the moon
    moon = ephem.Moon()
    
    # Calculate the phase of the moon
    moon.compute(observer)

    #ret
    return moon.moon_phase
 
def GetMoonPhasePar(datepar):
    # Define the observer's location
    observer = ephem.Observer()
    observer.lat = '54.7261409'
    observer.long = '55.947499'
    
    # Define the date
    observer.date = datepar
    #'2023/02/03'
    
    # Define the moon
    moon = ephem.Moon()
    
    # Calculate the phase of the moon
    moon.compute(observer)

    #ret
    return moon.moon_phase
 
# Print the phase of the moon
#print(moon.moon_phase)