class Analytics:
    def __init__(self, data):
        self._data = data

    def show_data(self):
        print(f"Data: {self._data}")


a = Analytics("Raw Data")
a.show_data()