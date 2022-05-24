import time
from reddit import reddit_scan

while True:
    time.sleep(8)
    reddit_scan()
    time.sleep(5) #cooldowns to prevent overloading of reddit api.