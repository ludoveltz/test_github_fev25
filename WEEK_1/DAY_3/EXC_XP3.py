class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

# Créer un objet Song
stairway = Song([
    "There’s a lady who's sure",
    "all that glitters is gold",
    "and she’s buying a stairway to heaven"
])

# Appeler la méthode sing_me_a_song
stairway.sing_me_a_song()