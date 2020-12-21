import json
import fbchat
from wappdriver import WhatsApp

def send_msg_over_whatsapp(msg):
    leszek_nr = "+48 500 320 191"
    andrea_nr = "+39 345 991 0527"
    with WhatsApp() as bot:
        bot.send(leszek_nr,  # name of recipient
                 msg  # message
                 )

    # name of recipient must be in contacts
    # You can also send images, videos, gifs, documents, urls, and other files
    # Visit aahnik.github.io/wappdriver for more info



def send_msg_over_facebook(msg):
    username = "malinowy.misiak@gmail.com"
    password = "hnewe13z2rd6r6"
    cookies = {}
    try:
        # Load the session cookies
        with open('session.json', 'r') as f:
            cookies = json.load(f)
    except:
        # If it fails, never mind, we'll just login again
        pass
    client = fbchat.Client(username, password, session_cookies=cookies, max_tries=1)
    with open('session.json', 'w') as f:
        json.dump(client.getSession(), f)
    andrzej_fb_id = 100000830152039
    leszek_fb_id = 109936953495929
    sent = client.send(fbchat.Message(text=msg), thread_id=andrzej_fb_id)
    if sent:
        print("Message sent successfully!")



if __name__ == '__main__':
    send_msg_over_facebook("Andrzej Notification Service test")
    send_msg_over_whatsapp("Andrzej Notification Service test")