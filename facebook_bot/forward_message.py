from fbchat import log, Client, ThreadType
from fbchat.models import *

class EchoBot(Client):

    def set_IDs(self, chat_with_id, forward_to_id, my_name, chat_with_name):
        self.chat_with_id = chat_with_id
        self.forward_to_id = forward_to_id
        self.my_name = my_name
        self.chat_with_name = chat_with_name


    def onMessage(self, author_id, message, thread_id, thread_type, **kwargspas ):
        # print("authorid = {}".format(author_id))
        # print("my id = {}".format(self.uid))
        # print(message)


        if author_id == self.chat_with_id:
            self.markAsDelivered(author_id, thread_id)
            self.markAsRead(author_id)

            mesg = self.chat_with_name + ": " + message
            self.sendMessage(mesg, thread_id=self.forward_to_id, thread_type=ThreadType.USER)
            print("case 1")


        elif author_id == self.uid:
            self.markAsDelivered(author_id, thread_id)
            self.markAsRead(author_id)

            mesg = self.my_name + ": " + message
            self.sendMessage(mesg, thread_id=self.forward_to_id, thread_type=ThreadType.USER)
            print("case 2")
        else:
            print("case 3")





email = "sss"
password = "ss"

u = "aaa"
p = "vvvvvvvvv"
chat_with_id = 'sdsdsd' 
forward_to_id = 'dsdsdsd' 
my_name = "sdsdsd"
chat_with_name = "sdsdsdsd"


client = EchoBot(u, p)
client.set_IDs(chat_with_id, forward_to_id, my_name, chat_with_name)


users = client.fetchAllUsers()

user=1

client.listen()


# print("User's ID: {}".format(user.uid))
# print("User's name: {}".format(user.name))
# print("User's profile picture url: {}".format(user.photo))
# print("User's main url: {}".format(user.url))

