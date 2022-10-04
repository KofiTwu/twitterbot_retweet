# Twitter Bot 
A sample Twitter bot in Python - that retweets based on a hashtag

---

## Set up notes

### How to install Tweepy

First, check your Python version with ``python3 --version`` or ``python --version`` on console (terminal/shell/command prompt).
Twwepy==3.7 was used for this project


#### If you have Python 3.x, you can just run:

``pip3 install tweepy``

#### If you have Python 3.7, run the following instead:

``pip3 install -U git+https://github.com/tweepy/tweepy.git@2efe385fc69385b57733f747ee62e6be12a1338b``

If the above command doesn't work, try replacing ``pip3`` with ``pip`` also.

#### If you have Python 3.7 and want to use pipenv, use:

``pipenv install -e git+https://github.com/tweepy/tweepy.git@2efe385fc69385b57733f747ee62e6be12a1338b#egg=tweepy``

---

## Files
- **twitter_bot.py** - This is the main file that includes all the logic.
- **api_keys_.py** - This file is not meant to be used directly. Instead, copy this file in the same folder and rename it to api_keys.py. Then, put your Twitter API keys in keys.py. That way, my_twitter_bot.py will be able to use this information.