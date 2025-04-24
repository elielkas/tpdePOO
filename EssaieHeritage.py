class Film:
    def __init__(self, name):
        self.name = name
    def watch(self):
        print("Bon visionnage")


class FilmCassette(Film):
    def __init__(self, name):
        self.name = name
        self.magnetic_tape = True
    def rewind(self):
        print("C'est long à rembobiner !")
        self.magnetic_tape = True


film = Film("2001: l'odyssee de l'espace")
film_cassette = FilmCassette("Blader Runner")

print(film_cassette.name)
print(film_cassette.magnetic_tape)
film_cassette.watch()
film_cassette.rewind()