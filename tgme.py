#!/usr/bin/env python3

# author:      vort3
# inspired by: https://github.com/marcotrosi/tgme

import urllib.request as request
import urllib.parse as parse
import sys
import os

def main():
    if len(sys.argv) == 1:
        print("""    NAME:
        tgme - send messages to your Telegram account

    SYNOPSIS:
        tgme "TEXT"
        tgme "TITLE" "TEXT"
        tgme "TITLE" "SUBTITLE" "TEXT"

    CONFIGURATION:
        The configuration shall consist of two files.
        One file named "token" shall contain the Telegram API token of your bot.
        A second file named "chatid" that shall contain the Telegram chat ID in which the bot is added.
        Use botfather within Telegram to create a bot and get a token for it.
        Add the bot and send a dummy message, then put "https://api.telegram.org/bot<YourBOTToken>/getUpdates"
        in your browser to find the chat_id.""")
        return

    if '-' not in sys.argv:
        if len(sys.argv)   == 2: message = sys.argv[1]
        elif len(sys.argv) == 3: message = f"<b>{sys.argv[1]}</b>\n\n{sys.argv[2]}"
        else:                    message = f"<b>{sys.argv[1]}</b>\n<i>{sys.argv[2]}</i>\n\n{' '.join(sys.argv[3:])}"
    else:
        message = "".join(sys.stdin.readlines())
        if message == "":
            return
        message = "<code>" + message + "</code>"

    configpath = os.path.join(os.path.expanduser("~"), ".config", "tgme")
    with open(os.path.join(configpath, "token")) as tokenfile:
        token = tokenfile.read().strip()
    with open(os.path.join(configpath, "chatid")) as chatidfile:
        chatid = chatidfile.read().strip()

    URL = f"https://api.telegram.org/bot{token}/sendMessage"
    data = parse.urlencode({"chat_id" : chatid, "text" : message, "parse_mode" : "HTML"})
    request.urlopen(f"{URL}?{data}")

if __name__ == "__main__":
    main()
