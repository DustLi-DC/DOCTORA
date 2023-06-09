import time

def pomodoro_timer(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
    
pomodoro_timer(25) # Set the number of minutes for the timer
