def make_album(artist_name,title,number_of_songs=None):
    album = {'Name': artist_name, 'Album' : title}
    if number_of_songs:
        album['Number of Songs'] = number_of_songs
    return album
    
cool=make_album('Slayer','Hell Awaits', 7)
print(cool)