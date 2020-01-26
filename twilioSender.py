from twilio.rest import Client  # Your Account Sid and Auth Token from twilio.com/console


def sendText(name, coords, number):
    account_sid = 'AC580d71ab92500c629896907390a74f42'
    auth_token = 'bb2b679214edab6f42938fda9c74e589'
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="{} - The Earthtones system has detected increased activity at the sensor with location {}. Please visit http://earthtones.online for a live view of the collected data.".format(name, coords),
        from_='+441404565052',
        to=number
    )
    print("{} - The Earthtones system has detected increased activity at the sensor with location {}. Please visit 'http://earthtones.online' for a live view of the collected data.".format(name, coords))

