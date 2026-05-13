class Machine:
    def start(self):
        print("Machine started.")


class Printer(Machine):
    def start(self):
        print("Printer started printing...")


p = Printer()
p.start()
