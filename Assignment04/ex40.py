class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

star_spangled = Song(["and the rockets' red glare",
                      "the bombs bursting in air"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

star_spangled.sing_me_a_song()
