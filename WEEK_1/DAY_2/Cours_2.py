# Dictionnaire de la playlist
playlist = {
    'title': "Hello World",
    'author': "Planet",
    'songs': [
        {
            'song_title': "Song One",
            'artist': ['Artist 1', 'Artist 2'],
            'duration': 4.31,
        },
        {
            'song_title': "Song Two",
            'artist': ['Artist 1'],
            'duration': 2.53,
        },
        {
            'song_title': "Song Three",
            'artist': ['Artist 1', 'Artist 2', 'Artist 3'],
            'duration': 3.43,
        }
    ]
}

# Calcul de la durée totale
total_duration = sum(song['duration'] for song in playlist['songs'])

# Afficher la durée totale
print(f"La durée totale de la playlist est de {total_duration} minutes.")