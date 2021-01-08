# class
# class Car():
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color
#         self.gas = 100

#     def __str__(self):
#         return '{}, {}, {}'.format(self.make, self.model, self.color)

#     def drive(self):
#         self.gas -= 10

#     def fill_tank(self):
#         self.gas = 100

#     def check_gas(self):
#         print(f"Gas handle: {self.gas}")


# car1 = Car('Mercedes', 'C300', 'white')

# car1.drive()
# car1.drive()
# car1.check_gas()
# car1.fill_tank()
# car1.check_gas()


class Computer():
    def __init__(self, make, device, color):
        self.make = make
        self.device = device
        self.color = color

    def __str__(self):
        return '{}, {}, {}'.format(self.make, self.device, self.color)


computer = Computer('Apple', 'MacBook M Chip', 'Grey')

print(computer)
