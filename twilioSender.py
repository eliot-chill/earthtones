from twilio.rest import Client  # Your Account Sid and Auth Token from twilio.com/console
import config


def sendText(name, coords, number):
    account_sid = config.getSSID()
    auth_token = config.getAuthToken()
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="{} - The Earthtones system has detected increased activity at the sensor with location {}. Please visit http://earthtones.online for a live view of the collected data.".format(name, coords),
        from_='+441404565052',
        to=number
    )
    print("{} - The Earthtones system has detected increased activity at the sensor with location {}. Please visit 'http://earthtones.online' for a live view of the collected data.".format(name, coords))

