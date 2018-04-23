import sys
import requests

def send_simple_message(apiKey, server, emailFrom, to, scriptName="script value not set", msg="msg value not set"):
    if not to or not apiKey or not server or not emailFrom:
        sys.exit(0)

    requests.post(
            server,
            auth=("api", apiKey),
            data={"from": emailFrom,
                  "to": to,
                  "subject": scriptName,
                  "text": msg})
