#coding:utf-8
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = "smtp.yeah.net"      # SMTP服务器
mail_user = ""                  # 用户名
mail_pass = "5"               # 授权密码，非登录密码  


sender = ""
receivers = "" #密码


message = MIMEMultipart()
title = '人生苦短'  # 邮件主题
message.attach(MIMEText('学习邮件发送测试','plain', 'utf-8'))

#构造附件1，传送指定目录下的文件
att1 = MIMEText(open('D:\\pythonSmallProgram\\baiduPic\\baiduPic.py','rb').read(),'base64','utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment;filename="mytest.py"'
message.attach(att1)

def sendEmail():

	#message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
	#message = message.attach(MIMEText('学习邮件发送测试','plain', 'utf-8'))
	message['From'] = "{}".format(sender)
	message['To'] = ",".join(receivers)
	message['Subject'] = title

	try:
		smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
		smtpObj.login(mail_user, mail_pass)  # 登录验证
		smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
		print("mail has been send successfully.")
	except smtplib.SMTPException as e:
		print(e)
'''
def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
	email_client = smtplib.SMTP(SMTP_host)
	email_client.login(from_account, from_passwd)
	# create msg
	msg = MIMEText(content, 'plain', 'utf-8')
	msg['Subject'] = Header(subject, 'utf-8')  # subject
	msg['From'] = from_account
	msg['To'] = to_account
	email_client.sendmail(from_account, to_account, msg.as_string())

	email_client.quit()
'''
if __name__ == '__main__':
	sendEmail()
	# receiver = '***'
	# send_email2(mail_host, mail_user, mail_pass, receiver, title, content)

