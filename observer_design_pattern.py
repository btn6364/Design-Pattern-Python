class YoutubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = [] 

    def add_subscriber(self, subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update(self)

class Subscriber:
    def __init__(self, name): 
        self.name = name

    def update(self, yt_channel):
        print(f"Hey {self.name}, {yt_channel.name} just released a new video!")

if __name__=="__main__": 
    yt_channel = YoutubeChannel("Bao Nguyen")
    sub1 = Subscriber("sub1")
    sub2 = Subscriber("sub2")
    sub3 = Subscriber("sub3")

    yt_channel.add_subscriber(sub1)
    yt_channel.add_subscriber(sub2)
    yt_channel.add_subscriber(sub3)
    yt_channel.notify_subscribers()

    print(f"\nRemoving sub1")
    yt_channel.remove_subscriber(sub1)
    yt_channel.notify_subscribers()





