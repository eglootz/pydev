from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC5f3432bd6681456092bf2b1f8cf1595c"
# Your Auth Token from twilio.com/console
auth_token = "c06e2d77fbc23b44d6696d99e54f851b"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+491711543256",
    from_="+17752567217",
    body="EIN TEST!")

print(message.sid)
