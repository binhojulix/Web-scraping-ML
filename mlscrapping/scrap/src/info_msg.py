
from threading import Thread

class MSG(Thread):

    def __init__(self):
        Thread.__init__(self)

    def msg(self):
        while(1):
            print("waiting...")
        
    def run(self):
        self.msg()