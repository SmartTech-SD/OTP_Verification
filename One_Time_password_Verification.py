import random
from twilio.rest import Client
otp=random.randint(100000,1000000)
print(otp)
# twilio account and token
account_sid='AC1cd45e881aa4008a3ec7a1d2d8e1f582'
auth_token='5e958a39090348c18a5c9100328dec67'
client=Client(account_sid,auth_token)
# user input
mobile_no=input("Enter your mobile number with cuntry code: ")
print(mobile_no)
# for sending otp verification message
message=client.messages.create(
body=f"Your otp verification code is :{str(otp)} Don't share this code with others ",
to=mobile_no,
from_='+12517584907'
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
