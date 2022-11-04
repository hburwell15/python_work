def make_album(artist_name, album_title):
    '''Display an artitsts name and album title'''
    album = {'artist': artist_name, 'album': album_title}
    return album

while True:
    print("\nTell me your favorite artist: ")
    print("(enter 'q' at any time to quit)")
    response = input("Artist name: ")
    if response == 'q':
        break

    print("\nWhat is the name of one of their albums? ")
    response_2 = input("Album title: ")
    if response_2 == 'q':
        break

    cd = make_album(response, response_2)
    print(cd)

print("\n")