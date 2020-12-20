import random
from twilio.rest import Client
otp=random.randint(100000,1000000)
# twilio account and token
account_sid=''
auth_token=''
client=Client(account_sid,auth_token)
# user input
mobile_no=input("Enter your mobile number with cuntry code: ")
# for sending otp verification message
message=client.messages.create(
body=f"Your otp verification code is :{str(otp)} Don't share this code with others ",
to=mobile_no,
from_='+125175849078090'
)
print(message.sid)
while True:
    recived_otp=int(input('Enter 6 digit otp here: '))
    if otp==recived_otp:
        print('your mobile number successfully resistred')
        break
    else:
        print('Incorrect otp')
        continue
