# Daily Paper
<img src="https://github.com/jaschers/daily-paper/blob/main/logo/logo.png" width="500">
Daily Paper searches and opens papers on [arXiv](https://arxiv.org/) that were uploaded on the previous day. The papers will be selected, opened and documented based on the keywords you specify.

## Requirements
You need:
* Python 3.8.5 or higher
* an arXiv account (register [here](https://arxiv.org/login))
* a gmail account (register [here](https://www.google.com/intl/en/gmail/about/))

## Setup
* clone the repository into your preferred folder `git clone git@github.com:jaschers/Daily Paper
<img src="https://github.com/jaschers/daily-paper.git`
* create a app password for your gmail account (see [here](https://support.google.com/accounts/answer/185833?hl=en) for instructions)
* sign up for arXiv daily to receive an email from arXiv each day
* run `python main.py`
  * enter your google email address
  * enter your google app password
  * enter your keywords separated with a comma, e.g. `dark matter,milky way,cosmic rays,hubble tension`
Daily paper searches for your keywords in the title and abstract in each paper uploaded on arXiv on the previous day. Once set up, you won't have to fill in your user information again. You can change your email address or password in `setup/user_info.txt` and your keywords in `setup/keywords.txt`/blob/main/logo/logo.png" width="500">
Daily Paper searches and opens papers on [arXiv](https://arxiv.org/) that were uploaded on the previous day. The papers will be selected, opened and documented based on the keywords you specify.

## Requirements
You need:
* Python 3.8.5 or higher
* an arXiv account (register [here](https://arxiv.org/login))
* a gmail account (register [here](https://www.google.com/intl/en/gmail/about/))

## Setup
* clone the repository into your preferred folder `git clone git@github.com:jaschers/daily-paper.git`
* create a app password for your gmail account (see [here](https://support.google.com/accounts/answer/185833?hl=en) for instructions)
* sign up for arXiv daily to receive an email from arXiv each day
* run `python main.py`
  * enter your google email address
  * enter your google app password
  * enter your keywords separated with a comma, e.g. `dark matter,milky way,cosmic rays,hubble tension`
Daily paper searches for your keywords in the title and abstract in each paper uploaded on arXiv on the previous day. Once set up, you won't have to fill in your user information again. You can change your email address or password in `setup/user_info.txt` and your keywords in `setup/keywords.txt`

## Usage
Run `python main.py` and enjoy your daily dose of paper! The papers are opened in your default webbrowser and documented in `links/<yyyy>-<mm>-<dd>.txt` sorted by your keywords.