def make_album(artist_name, album_title, number_of_songs=None):
    """Create a dictionary with information about an album."""
    
    artist_name_formatted = artist_name.title()
    album_title_formatted = album_title.title()
    
    if number_of_songs:     # Handle optional parameter for number of songs
        album = {
            'artist': artist_name_formatted, 
            'album': album_title_formatted,
            'number of songs' : number_of_songs,
            }
    else:
        album = { 
                 'artist': artist_name_formatted, 
                 'album': album_title_formatted,
                 }
    return album

album_1 = make_album('jewel', 'pieces of you')
album_2 = make_album('spice girls', 'spice world', 10)
album_3 = make_album('grimes', 'geidi primes', 11)

print(album_1)
print(album_2)
print(album_3)