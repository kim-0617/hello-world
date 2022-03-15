from imap_tools import MailBox
from account import *

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # for msg in mailbox.fetch():
    #     print(f"[{msg.from_}] {msg.subject}")

    # for msg in mailbox.fetch('(UNSEEN)'): # 읽지 않은 메일 가져오기
    #     print(f"[{msg.from_}] {msg.subject}")

    # for msg in mailbox.fetch('(FROM kimsh5993@gmail.com)'): # 특정인이 보낸 메일 가져오기
    #     print(f"[{msg.from_}] {msg.subject}")

    # for msg in mailbox.fetch('(TEXT "test mail")'): # 어떤 글자를 포함하는 메일
    #     print(f"[{msg.from_}] {msg.subject}")

    # for msg in mailbox.fetch('(SUBJECT "test mail")'): # 특정 제목 검색
    #     print(f"[{msg.from_}] {msg.subject}")

    # for msg in mailbox.fetch(limit=5, reverse=True): # 제목이 한글을 포함할 때 처리 방법
    #     if "테스트" in msg.subject:
    #         print(f"[{msg.from_}] {msg.subject}")

    # for msg in mailbox.fetch(f'(SENTSINCE 27-Jan-2021)',reverse=True, limit=5): # 특정 날짜 이후에 온 메일 검색
    #     print(f"[{msg.from_}] {msg.subject}")

    # for msg in mailbox.fetch('(ON 25-Jan-2022)'): # 특정날짜에 온 메일
    #     print(f"[{msg.from_}] {msg.subject}")

    # # 2가지 이상의 조건을 모두 만족하는 메일
    # for msg in mailbox.fetch('(SENTSINCE 27-Jan-2021 SUBJECT "test mail")',reverse=True, limit=5):
    #     print(f"[{msg.from_}] {msg.subject}")

    # 2가지의 조건을 하나라도 만족하는 메일
    for msg in mailbox.fetch('(OR SENTSINCE 27-Jan-2021 SUBJECT "test mail")',reverse=True, limit=5):
        print(f"[{msg.from_}] {msg.subject}")