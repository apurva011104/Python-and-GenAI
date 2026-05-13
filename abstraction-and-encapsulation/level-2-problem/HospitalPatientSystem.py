class Patient:
    def __init__(self, name, disease):
        self.__name = name
        self.__disease = disease

    def get_info(self):
        return f"Patient: {self.__name} | Disease: Confidential"


p = Patient("John", "Flu")
print(p.get_info())