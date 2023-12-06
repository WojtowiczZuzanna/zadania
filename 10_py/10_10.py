class Music():
    def __init__(self,artist, track_title, album, year):
        self.artist = artist
        self.track_title = track_title
        self.album = album
        self.year = year

    def __str__(self,artist, track_title, album, year):
        return f'Performer: {self.artist}\nSong: {self.track_title}\nAlbum: {self.album}\nYear: {self.year}'

music1 = Music("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
print(music1)

music2 = Music(
    ...
)