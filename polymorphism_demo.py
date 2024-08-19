class Bird:
    def fly(self):
        print('Flying in the sky!')

class Penguin(Bird):
    def fly(self):
        print('I can\'t fly but I can swim!')

if __name__ == "__main__":
    birds = [Bird(), Penguin()]
    for bird in birds:
        bird.fly()