#import the required modules
import requests

print('This is tool is made by Van Beethoven Arne, Have fun!!')

#start with giving the client info
client_id = input ('give your client id: ')
client_secret = input ('give your client secret: ')

#check if the client info is correct
if client_secret == "" or client_id == "":
    print("please give the right information from the client")


first_url = "https://accounts.spotify.com/api/token"


auth_response = requests.post(first_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })
#converting to json
auth_response_data = auth_response.json()

#save the token as access_token
access_token = auth_response_data['access_token']

headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

#get yhe url from the spotify api
base_url = 'https://api.spotify.com/v1/search?'

#ask the user for input
print()
artist = input('Enter the name of your favourite artist: ')
print()


try:
    r = requests.get(base_url + 'q=' + artist + '&type=artist&market=US&limit=1', headers=headers)
    r = r.json()

   
    followers = r['artists']['items'][0]['followers']['total']

    artist_id = r['artists']['items'][0]['id']
    url = 'https://api.spotify.com/v1/'

    r = requests.get(url + 'artists/' + artist_id + '/albums', headers=headers, params={'include_groups': 'album'})
    d = r.json()

    chosen_artist = d['items'][0]['artists'][0]['name']

    #print the information about the artist
    print('u searched for ', chosen_artist)
    print()
    print(artist, ' has ', followers, ' followers')
    print()
    print('he has those albums: ')


    
    for album in d['items']:
        album_name = album['name']
        album_tracks = album['total_tracks']


       #print the albums and their total tracks they contain
        print('- ',album_name,' has ', album_tracks,' songs on it.')

        
except:    
    print("This Artist cannot be found, try another one please")
