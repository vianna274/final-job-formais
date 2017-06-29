class Terminal():
    def __init__(self, value, genre, number):
        self.setValue(value)
        self.setGenre(genre)
        self.setNumber(number)

    def __str__(self):
        return " " + str(self.value)

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def setGenre(self, genre):
        self.genre = genre

    def getGenre(self):
        return self.genre

    def setNumber(self, number):
        self.number = number

    def getNumber(self):
        return self.number

    def getClass(self):
        return "Terminal"
