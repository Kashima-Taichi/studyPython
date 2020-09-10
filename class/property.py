class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')


class ToyotaCar(Car):
    def run(self):
        print('fast')


class TeslaCar(Car):
    def __init__(self, model='Model S', enable_auto_run=False):
        super().__init__(model)
        self._enable_auto_run = enable_auto_run

    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    def run(self):
        print('super fast')

    def auto_run(self):
        print('auto run')


car = Car()
car.run()

toyota_car = ToyotaCar('Lexus')
print(toyota_car.model)
toyota_car.run()

tesla_car = TeslaCar('Model S')
tesla_car.enable_auto_run = True
print(tesla_car.enable_auto_run)
print(tesla_car.model)
tesla_car.run()
tesla_car.auto_run()

