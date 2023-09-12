#make_album

# records = []

def make_album(artist_name,album_title,number_of_songs=None):
    albumdict = {
        'Name': artist_name.title(),
        'Album' : album_title.title()
          }
    if number_of_songs:
        albumdict['Number of Songs'] = number_of_songs
    return albumdict
    
# cock_prompts
title_prompt = "\nWhat album are you thinking of?: "
artist_prompt = "Who's the artist?:  "
songs_prompt = "How many songs are on that album?: "

# Let the user know how to fuck off.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break
    
    number_of_songs = input(songs_prompt)
    if number_of_songs == 'quit':
        break

    album = make_album(artist, title, number_of_songs)
    print(album)

print("\nThanks for responding!")



