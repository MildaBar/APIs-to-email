import os
import sys
import json
import smtplib
import requests
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


# check if the format of the command line arguments is valid
def check_input():
    if len(sys.argv) == 3:
        # check provided email
        if "@" not in sys.argv[1] or "." not in sys.argv[1]:
            print("Format of email is not valid. Try again.")
            sys.exit()
        # check whether the API argument passed is one of the two that you have implemented
        elif sys.argv[2] != "quotes_api" and sys.argv[2] != "weather_api":
            print("Format of API is not valid. Try again.")
            sys.exit()
        else:
            email = sys.argv[1]
            api = sys.argv[2]
            send_email(email, api)
    else:
        print("Usage: <python> <file_name.py> <email adress> <API>")
        sys.exit()
    return email, api


def quotes_api():
    # request API
    quotes_api = requests.get("https://api.themotivate365.com/stoic-quote")
    o_quotes_api = quotes_api.json()

    # find quote and author
    quote = o_quotes_api["quote"]
    author = o_quotes_api["author"]

    # message variable
    quote_message = f"'{quote}' by {author.upper()}"
    return quote_message


def weather_api():
    # request API
    weather_api = requests.get(
        "https://api.open-meteo.com/v1/forecast?latitude=54.69&longitude=25.28&hourly=temperature_2m&current_weather=true"
    )
    o_weather_api = weather_api.json()


    # find current temperature
    current_temp = o_weather_api["current_weather"]["temperature"]

    # message variable
    temp_message = f"Current temperature in Vilnius: {current_temp}°C"
    return temp_message


def send_email(email, api):
    
    # create an instance of the EmailMessage class
    msg = EmailMessage()

    if api == "quotes_api":
        email_message = quotes_api()
        msg.set_content(email_message)
    elif api == "weather_api":
        email_message = weather_api()
        msg.set_content(email_message)

    # set the subject, sender of the message and the resipient of the email message
    msg["Subject"] = "Email from Python"
    msg["From"] = "Milda Ba."
    msg["To"] = email

    # create an instance of SMTP class with server name and port number
    my_server = smtplib.SMTP("smtp.gmail.com", 587)

    # starts TLS connection
    my_server.starttls()

    # get access to password and email
    password = os.getenv("PASSWORD")
    my_email = os.getenv("EMAIL")

    # logs in to Gmail account using name and password
    my_server.login(my_email, password)

    # send the message using SMTP server
    my_server.send_message(msg)

    # quits SMTP server
    my_server.quit()

    print("Email sent successfully")


def main():
    while True:
        try:
            check_input()
            break

        except ValueError:
            pass


if __name__ == "__main__":
    main()

# keybinds:
# 1. ctrl + l = select current line
# 2. ctrl + d = add selection to next find match
# 3. ctrl + x = cut line and copy it
# 4. tab; shift + tab
# 5. ctrl + enter = insert line below