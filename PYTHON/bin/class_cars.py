class cars:
    def __init__(self, make, model, year, top_speed, engine, engine_volume, number_built):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self.engine = engine
        self.engine_volume = engine_volume
        self.number_built = number_built

    def __add__(self, make):
        assert isinstance(make, object)
        self.make = make

    def __str__(self):
        return f"""{self.make} {self.model} made on {self.year}, Max speed reached is {self.top_speed}.
Came with a {self.engine } and {self.engine_volume} in volume.
They are about {self.number_built} in the world"""
