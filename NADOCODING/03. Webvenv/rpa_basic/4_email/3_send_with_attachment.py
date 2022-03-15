import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다" # 제목
msg["From"] = EMAIL_ADDRESS # 보내는곳
msg["To"] = "kimsh5993@gmail.com" # 보낼곳
msg.set_content("다운로드 하세요") # 본문

# msg.add_attachment()
with open("피디프.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype = "application", subtype= "pdf", filename = f.name)

with open("sample.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype = "application", subtype= "vnd.ms-excel", filename = f.name)

with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)