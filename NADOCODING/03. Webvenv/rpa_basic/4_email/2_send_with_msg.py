import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다" # 제목
msg["From"] = EMAIL_ADDRESS # 보내는곳
msg["To"] = "kkk5993@naver.com" # 보낼곳
msg.set_content("테스트 본문입니다.") # 본문

# # 여러 명에게 메일을 보낼 때
# msg["To"] = "주소1", "주소2", "주소3"
# or
# to_list = ["주소1", 주소2, 주소3]
# msg["To"] = ", ".join(to_list) # ,로 구분해서 합친다

# # 참조
# msg["Cc"] = "주소"

# # 비밀 참조
# msg["Bcc"] = "주소"

with smtplib.SMTP("smtp.gmail.com",587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)