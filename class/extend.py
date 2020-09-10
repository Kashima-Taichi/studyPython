class Car(object):
    # passは何もしないという意味である
    # pass
    def run(self):
        print('run')


class ToyotaCar(Car):
    # passは何もしないという意味である
    pass


class TeslaCar(Car):
    def auto_run(self):
        print('auto run')


car = Car()
car.run()

toyota_car = ToyotaCar()
toyota_car.run()

tesla_car = TeslaCar()
tesla_car.run()
tesla_car.auto_run()
