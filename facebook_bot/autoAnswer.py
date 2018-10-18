from fbchat import log, Client


class EchoBot(Client):
    def onMessage(self, author_id, message, thread_id, thread_type, **kwargspas ):
        self.markAsDelivered(author_id, thread_id)
        self.markAsRead(author_id)


        if author_id != self.uid:
            self.sendMessage(message, thread_id=thread_id, thread_type=thread_type)


email = "ddddd"
password = "ddddd"

u = "ad"
p = "aaad"

client = EchoBot(u, p)
client.listen()