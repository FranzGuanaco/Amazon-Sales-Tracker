class Pierre:
    def __init__(self,name):
        self.name = name
        self.firstname = 'Chevin'

    def read(self):
        print(self.name)

class test (Pierre):
    def arg (self,name):
        Pierre.__init__(self,name)


x = test('Pierre')
x.read()


