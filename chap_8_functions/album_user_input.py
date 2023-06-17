def make_album(artist_name, album_title):
    """Create a dictionary with information about an album."""
    
    # Format the arguments. Not sure if this is the best place to do this.
    
    artist_name_formatted = artist_name.title()
    album_title_formatted = album_title.title()
    
    # Build the dictionary.
    
    album = { 
                 'artist': artist_name_formatted, 
                 'album': album_title_formatted,
                 }
    return album


# Take user inputs for artist name and album title

while True:
    print("\nStoring information about your favorite albums..."
          "\nPress 'q' at any time to quit.")
    
    input_artist_name = input("What is the artist's name? ")
    if input_artist_name.lower() == 'q': # Exit the loop if the user quits
        break

    input_album_title = input("what is the title of the album? ")
    if input_album_title.lower() == 'q': # Exit the loop if the user quits
        break

    # Use make_album() to build and display a dictionary with this information. 
    
    print(make_album(input_artist_name, input_album_title))