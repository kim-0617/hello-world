from email.mime import application
from imap_tools import MailBox
from account import *

applicant_list = [] # 지원자 리스트

with MailBox('imap.gmail.com', 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    index = 1 # 순번
    for msg in mailbox.fetch('(SENTSINCE 28-Jan-2022)'):
        if "파이썬 특강 신청합니다." in msg.subject:
            nickname, phone = msg.text.strip().split('/')
            # print(nickname, phone, index)
            applicant_list.append((msg,index,nickname,phone))
            index += 1

# for applicant in applicant_list:
#     print(applicant)