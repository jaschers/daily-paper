import readline
import numpy as np
import os
import datetime
import webbrowser
import imaplib
import email
from email.header import decode_header

########################################## SETUP ##########################################
# To setup a google app password vist: https://support.google.com/accounts/answer/185833?hl=de

if os.path.exists("setup/user_info.txt") == False and os.path.exists("setup/keywords.txt") == False:
    # create setup directory
    os.mkdir("setup", exist_ok = True)

    # ask for user input
    user_email = input("Enter your google email address: ")
    user_password = input("Enter your google app password: ")
    user_keywords = input("Enter your paper keywords (separate with ','): ")

    # write input into .txt files
    file_user = open("setup/user_info.txt", "w")
    file_user.write("User email address, user app password\n")
    file_user.write(f"{user_email}\n")
    file_user.write(f"{user_password}\n")

    file_keywords = open("setup/keywords.txt", "w")
    file_keywords.write(f"{user_keywords}")

    USERNAME = user_email
    PASSWORD = user_password
    KEYWORD = user_keywords.split(",")

else:
    # read the setup files
    file_user = open("setup/user_info.txt", "r")
    lines_user = file_user.read().splitlines()[1:]
    file_user.close()

    USERNAME = lines_user[0]
    PASSWORD = lines_user[1]

    file_keywords = open("setup/keywords.txt", "r")
    lines_keywords = file_keywords.readlines()

    KEYWORD = lines_keywords[0].split(",")

########################################## INPUT ##########################################
ARXIV_KEYWORD = "https://arxiv.org"
date = f"{datetime.datetime.now():%Y-%m-%d}"

PATH_FOLDER = "links/"
PATH_OUTPUT = "links/{0}.txt".format(date)

########################################## GET EMAIL ##########################################
# code from https://www.thepythoncode.com/article/reading-emails-in-python

# create an IMAP4 class with SSL
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(USERNAME, PASSWORD)

status, messages = imap.select("INBOX")
# number of top emails to fetch
N = 100
# total number of emails
messages = int(messages[0])

for i in range(messages, messages-N, -1):
    # fetch the email message by ID
    res, msg = imap.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject = decode_header(msg["Subject"])[0][0]

            # decode email sender
            From, encoding = decode_header(msg.get("From"))[0]
            if From == "no-reply@arXiv.org (send mail ONLY to astro-ph)":
                # extract content type of email
                content_type = msg.get_content_type()
                # get the email body
                text_input = msg.get_payload(decode=True).decode()
    if From == "no-reply@arXiv.org (send mail ONLY to astro-ph)":
        break

# close the connection and logout
imap.close()
imap.logout()

########################################## SAVE WEBSITES ##########################################
os.makedirs(PATH_FOLDER, exist_ok = True)

# open txt file to save paper links
file_output = open(PATH_OUTPUT, "w")

# split each paper contained in the email
individual_paper = text_input.split("------------------------------------------------------------------------------")

websites = np.array([])
counter = np.zeros(len(KEYWORD))

for j in range(len(KEYWORD)):
    file_output.write("{0}\n".format(KEYWORD[j].strip()))
    for i in range(len(individual_paper)):
        if KEYWORD[j].lower() in individual_paper[i].lower():
            lines = individual_paper[i].split("\n")
            for k in range(len(lines)):
                if ARXIV_KEYWORD in lines[k]:
                    websites = np.append(websites, lines[k][5:37])
                    file_output.write("{0} \n".format(lines[k][5:37]))
                    counter[j] += 1

    file_output.write("------------------------------------------------ \n")

print("{0} new arXiv paper today!".format(len(individual_paper)))
for i in range(len(KEYWORD)):
    print("{0} {1}".format(int(counter[i]), KEYWORD[i].strip()))

# remove dublicates
websites = list(set(websites))

# open the websites
for i in range(len(websites)):
    webbrowser.open("{0}".format(websites[i]))
