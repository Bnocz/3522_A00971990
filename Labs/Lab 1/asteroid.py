class Asteroid ():
    id = 0
    def __init__(self, radius, position, velocity, timestamp, id):
        self.radius = radius
        self.position = position
        self.velocity = velocity
        self.timestamp = timestamp
        self.id +=1

    def get_id(self):
        return self.id

    def get_timestamp(self):
        return self.timestamp

    def get_radius(self):
        return self.radius

    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velocity