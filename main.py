import spotipy
from spotipy.oauth2 import SpotifyOAuth

def authenticate_spotify():
    # Fill in your client ID, client secret, and redirect URI
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    redirect_uri = 'YOUR_REDIRECT_URI'

    # Set up authentication
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))
    return sp

def get_user_tracks(sp):
    # Retrieve the user's saved tracks
    results = sp.current_user_saved_tracks()
    return results['items']

def generate_recommendations(sp, seed_track_id):
    # Generate song recommendations
    recommendations = sp.recommendations(seed_tracks=[seed_track_id], limit=5)
    return recommendations['tracks']

if __name__ == '__main__':
    sp = authenticate_spotify()
    user_tracks = get_user_tracks(sp)
    for idx, item in enumerate(user_tracks):
        track = item['track']
        print(f"{idx + 1}. {track['name']} by {track['artists'][0]['name']}")

    seed_track_id = input("Enter the ID of the track for recommendations: ")
    recommendations = generate_recommendations(sp, seed_track_id)
    for idx, track in enumerate(recommendations):
        print(f"Recommendation {idx + 1}: {track['name']} by {track['artists'][0]['name']
