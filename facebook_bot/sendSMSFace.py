import pickle

import fbchat

from fbchat import Client
from fbchat.models import *

# from getpass import getpass
username = "fffff"
password = "ffffff"

u = "ffefefef"
p = ""

client = fbchat.Client(u, p)

Hieu_ID = 1111
Vyid = 111
messages = client.fetchThreadMessages(thread_id = Vyid, limit=999)
messages.reverse()


MAX_PRINTED = 100
for i in range(MAX_PRINTED):
    print(messages[i].text)

print(type(messages))

print("done")




# print('Own id: {}'.format(client.uid))
# client.sendMessage('Hi me!', thread_id=client.uid, thread_type=ThreadType.USER)

# client.sendEmoji(emoji='👍', size=EmojiSize.LARGE, thread_id=client.uid, thread_type=ThreadType.USER)

threads = client.fetchThreadList()

# print("users' IDs: {}".format(user.uid for user in users))
# print("users' names: {}".format(user.name for user in users))



client.logout()





