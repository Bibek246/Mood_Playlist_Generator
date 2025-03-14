import requests

def get_spotify_token():
    """
    Get Spotify API access token.
    """
    client_id = "92ca87840aa342b6bd941298950978dc"
    client_secret = "395e2b336cca41b3b39bdf2e28edf779"

    auth_response = requests.post(
        'https://accounts.spotify.com/api/token',
        data={'grant_type': 'client_credentials'},
        auth=(client_id, client_secret)
    )
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']

def get_spotify_categories():
    token = get_spotify_token()
    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(
        'https://api.spotify.com/v1/browse/categories',
        headers=headers
    )
    if response.status_code == 200:
        categories = response.json().get('categories', {}).get('items', [])
        return {category['id']: category['name'] for category in categories}
    else:
        raise Exception(f"Failed to retrieve categories: {response.status_code}")

# Fetch and print available categories
categories = get_spotify_categories()
print(categories)
