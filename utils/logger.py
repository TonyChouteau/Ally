
class Logger:

    __debug = True

    def __init__(self, tag):
        self.tag = tag

    def log(self, *messages):
        if self.__debug:
            print(" -", self.tag, "- ")
            for message in messages:
                print(message)
