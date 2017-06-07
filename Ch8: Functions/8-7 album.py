def make_album(artist_name, album_title, num_tracks=''):
    """Return a dictionary of an artist"""
    artist = {'artist name': artist_name, 'album': album_title}
    if num_tracks:
        artist['tracks'] = num_tracks
    return artist
while True:
    print("\nEnter artist, album, and optionally number of tracks.")
    print("enter 'q' at any time to quit")

    artist = input("artist: ")
    if artist == 'q':
        break
    album = input("album: ")
    if album == 'q':
        break
    tracks = input("optionally number of tracks: ")
    if tracks == 'q':
        break
    dictionary = make_album(artist, album, tracks)

    print("\nHere it is", dictionary)

