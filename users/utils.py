from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACc0071f3956151467940911f5b1a9279b'
auth_token = '2d5c4e0c8ff352ea72f1ba67c0477554'
client = Client(account_sid, auth_token)


def send_sms(user_code, phone_number):
    message = client.messages \
        .create(
        body=f"{user_code}",
        from_='+12018854146',
        to=f'{phone_number}'
    )

    print(message.sid)
