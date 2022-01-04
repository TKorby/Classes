class Animal:
    def __init__(self, name, colors, size, sex, age):
        self.name = name
        self.colors = colors
        self.size = size
        self.sex = sex
        self.age = age
        self.hunger = 0
        self.thirst = 0
        self.positionX = 0
        self.positionY = 0
        self.positionZ = 0

    def move_left(self):
        self.positionX -= 1

    def move_right(self):
        self.positionX += 1

    def move_forward(self):
        self.positionY += 1

    def move_backward(self):
        self.positionY -= 1

    def get_name(self):
        return self.name

    def get_colors(self):
        return self.colors

    # etc

    def make_noise(self):
        if self.size == "tiny":
            noise_mult = 0.1
            print('meep')
        elif self.size == "small":
            noise_mult = 0.25
            print('Meep')
        elif self.size == "medium":
            noise_mult = 0.6
            print('Meeeep')
        elif self.size == "large":
            noise_mult = 0.8
            print('MEEP')
        else:
            noise_mult = 1
            print('MEEEEEEEEP')

    def eat(self, food_saturation):
        if self.hunger - food_saturation <= 0:
            self.hunger = 0
        else:
            self.hunger -= food_saturation

    def drink(self, thirst_saturation):
        if self.thirst - thirst_saturation <= 0:
            self.thirst = 0
        else:
            self.thirst -= thirst_saturation


class Book:
    def __init__(self, title, author, pagecount, genre, publication, data):
        self.title = title
        self.author = author
        self.pagecount = pagecount
        self.genre = genre
        self.publication = publication
        self.current_page = 0
        self.bookdata = data

    def get_current_page_data(self):
        return self.bookdata[self.current_page]

    def get_page_number(self):
        return self.current_page


class Vehicle:
    def __init__(self, make, model, year, licenseplate, gears, specialkey):
        self.make = make
        self.model = model
        self.year = year
        self.licenseplate = licenseplate
        self.gears = gears
        self.specialkey = specialkey
        self.engineOn = False
        self.speed = 0
        self.current_gear = 0

    def toggleEngineState(self, key):
        if key == self.specialkey:
            if self.engineOn is False:
                self.engineOn = True
            else:
                self.engineOn = False

    def brake(self, pedal):
        if pedal > 0:
            if self.speed - (15 * pedal) <= 0:
                self.speed = 0
            else:
                self.speed -= (15 * pedal)

    def accelerate(self, pedal):  # would need to include a lot more to be realistic
        if pedal > 0:
            if self.speed + (15 * pedal) <= 200:
                self.speed = 200
            else:
                self.speed += (15 * pedal)

    def shiftAutomatic(self, direction):
        if direction == "up":
            if self.current_gear + 1 <= self.gears:
                self.current_gear += 1
        elif direction == "down":
            if self.current_gear - 1 >= 0:
                self.current_gear -= 1

    def shiftManual(self, shiftslot, clutch, pedal):
        if clutch >= 0.83 and pedal < 0.15:
            self.current_gear = shiftslot
        else:
            print("This ain't gonna be good.")
