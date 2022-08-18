class david:
    def __init__(self, name):
        self.name = name
        print("initialized")

    def hello(self):
        print("hello" + self.name + "!")
    
    def goodbye(self):
        print("Good bye" + self.name + "!")
m=david(" saa")
m.hello()
m.goodbye()