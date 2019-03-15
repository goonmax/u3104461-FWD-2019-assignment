import webbrowser
import time 
import random

while True:
    sites = random.choice(['google.com', 'facebook.com', 'youtube.com'])
    vist = "http://{}".format(sites)
    webbrowser.open(vist)
    seconds = random.randrange(5, 20)
    time.sleep(seconds)