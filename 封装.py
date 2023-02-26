class test2:
    def __init__(self, mode1):
        self.mode1 = mode1
        self.bullet_count = 0

    def add(self, count):
        self.bullet_count += count


class Test1:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def eat(self):
        print('喜欢吃 %s' % self.name)
        self.gun

tets2 = test2
test = Test1('nihao')
test.gun = tets2
test.gun.add(1,10)
test.eat()
