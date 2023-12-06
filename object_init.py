# coding:utf-8

class Person(object):
    name = None
    age = None

    def run(self):
        print(f'{self.name} 在奔跑')

    def jump(self):
        print(f'{self.name} 在跳跃')

    def sleep():
        print('在睡觉')

    def work(self):
        self.run()
        self.jump()
        def sleep(name):
            return name
        result = sleep(self.name)
        print('sleep result is ', result)

xiaomu = Person()
xiaomu.name = '小慕'
xiaomu.jump()
print('-----')
xiaomu.work()

