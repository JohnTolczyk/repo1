#make_album

records = []

def make_album(artist_name,title,number_of_songs):
    album = {'Name': band_name , 'Album' : record_name}
    if number_of_songs:
        album['Number of Songs'] = songs
    records.append(album)
    return album
    

while True:
    band_name = input("\nEnter name of band/artist: ")
    print("enter 'q' at anytime to quit.")
    if band_name == 'q':
        break
        

    record_name = input("\nEnter the name of one of their albums: ")
    print("enter 'q' at anytime to quit.")
    if record_name == 'q':
        break

    songs = input('\nhow many songs are on that album?: ')
    if songs == 'q':
        break
    
    print(records)

make_album(any,any,any)

