class Hammock:
    def __init__(self):
        self.nb_people = 0
        self.people_limit = 1
        self.last_to_ask = None

    def isEmpty(self):
        return self.nb_people == 0

    def sitDown(self, name):
        if self.isEmpty() or name == self.last_to_ask:
            self.nb_people += 1
            self.last_to_ask = name
            return "welcome!"
        else:
            self.last_to_ask = name
            return "sorry, no room"

    def leave(self):
        self.nb_people = max(0, self.nb_people - 1)
        return self.nb_people

## TESTS ##

myHammock = Hammock()
print(myHammock.sitDown('George'))
print(myHammock.sitDown('Bobby'))
print(myHammock.sitDown('Bobby'))
print(myHammock.leave())
print(myHammock.leave())
print(myHammock.leave())
print(myHammock.sitDown('Martha'))
print(myHammock.sitDown('Wilhelm'))
print(myHammock.sitDown('Klaus'))
print(myHammock.sitDown('Wilhelm'))
print(myHammock.leave())
