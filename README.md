# Daily Paper
<img src="https://github.com/jaschers/daily-paper/blob/main/logo/logo.png" width="500">
Daily Paper searches and opens papers on arXiv that were uploaded on the previous day. The papers will be selected, opened and documented based on the keywords you specify.

## Requirements
You need:
* Python 3.6 or higher
* a gmail account (register [here](https://www.google.com/intl/en/gmail/about/) for free)
* a subscription to the arXiv email alerting service (register [here](https://arxiv.org/help/subscribe) for free)
  * E.g. if you want to subscribe to the "Astrophysics" subject class and you are only interested in the "Cosmology and Nongalactic Astrophysics" and "High Energy Astrophysical Phenomena" subclass, you have to send an email as follows (a list of all subject classes can be found [here](https://arxiv.org/category_taxonomy)):
``` 
To: astro-ph@arxiv.org
Subject: subscribe <your name> 

add Cosmology and Nongalactic Astrophysics
add High Energy Astrophysical Phenomena
```

Note: before you proceed with the next steps, you need to wait (usually until the next morning) until you've received the first email from arXiv with a list of the most recent papers.

## Setup
* clone the repository into your preferred folder `git clone git@github.com:jaschers/daily-paper.git`
* create a app password for your gmail account (see [here](https://support.google.com/accounts/answer/185833?hl=en) for instructions)
* go to `daily-paper/` and run `python main.py`
  * enter your google email address
  * enter your google app password
  * enter your keywords separated with a comma, e.g. `dark matter,milky way,cosmic rays,hubble tension`

Daily paper searches for your keywords in the title and abstract in each paper uploaded on arXiv on the previous day (independent of the capitalisation of your keywords). Once set up, you won't have to fill in your user information again. You can change your email address or password in `setup/user_info.txt` and your keywords in `setup/keywords.txt`

## Usage
Run `python main.py` and enjoy your daily dose of paper! The papers are opened in your default webbrowser and documented in `links/<yyyy>-<mm>-<dd>.txt` sorted by your keywords. For your convinience, I'll recommend to add an alias into your `.bashrc` file, e.g. `alias dailypaper='python <your daily paper path>/main.py'`.

### References
https://www.thepythoncode.com/article/reading-emails-in-python
