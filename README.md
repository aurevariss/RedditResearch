# Reddit research project

## What it can do?
- Getting texts from reddit posts with urls and collect them in .txt file:
  - title
  - post body aka the post itself
  - all the comments (might work incorrectly with too long branches)
- Preparing texts for analysis:
  - get rid of punctuation
    - get rid of apostrophes (optional)
  - get rid of new lines, double spaces, tabs
  - get rid of numbers, emojis
  - lowering the case (optional)


## What's under development?
- Word frequency analysis
- (More be added)

## How to use:
In command line / shell:
- ```git clone !!!!!!!!!!!!!!!!!!!!!!!```
- ```cd !!!!!!!!!!!!!!!!!!!!!!!```
- ```pip3 install -r requirements.txt```
- ```cp config/config.cfg.sample config/config.cfg```

Populate values in ```config/config.cfg```:
- ```client_id``` = ID from [here](https://www.reddit.com/prefs/apps)
- ```client_secret``` = Secret from [here](https://www.reddit.com/prefs/apps)
- ```username``` = your Reddit username

> For more info about API and ID and secret watch [this video](https://youtu.be/1KJ_I5h8FRo?si=vZv1080kSBa74dMw&t=135)

In files:
- Add urls line by line in ```urls.txt```
