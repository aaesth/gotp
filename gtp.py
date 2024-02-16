import requests

def get_top_play(username):
    api_key = 'PUT AN API KEY HERE'  # Specifically the LEGACY api key, rtfreadme
    url = f'https://osu.ppy.sh/api/get_user_best?u={username}&limit=1&k={api_key}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        if data:
            return data[0]
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def get_accuracy(count50, count100, count300, countmiss):
    total_hits = count50 + count100 + count300 + countmiss
    if total_hits == 0:
        return 0
    return ((count50 * 50) + (count100 * 100) + (count300 * 300)) / (total_hits * 300) * 100

def get_beatmap_name(beatmap_id):
    api_key = 'PUT AN API KEY HERE'  # Specifically the LEGACY api key, rtfreadme
    url = f'https://osu.ppy.sh/api/get_beatmaps?b={beatmap_id}&k={api_key}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        if data:
            return data[0]['title']
        else:
            return "Unknown Beatmap"
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return "Unknown Beatmap"

def main():
    username = input("Enter osu! username: ")
    
    top_play = get_top_play(username)
    if top_play:
        beatmap_name = get_beatmap_name(top_play['beatmap_id'])
        accuracy = get_accuracy(int(top_play['count50']), int(top_play['count100']), int(top_play['count300']), int(top_play['countmiss']))
        mods = decode_mods(int(top_play['enabled_mods']))
        print("Top Play:")
        print(f"Beatmap: {beatmap_name}")
        print(f"PP: {top_play['pp']}")
        print(f"Accuracy: {accuracy:.2f}%")
        print(f"Max Combo: {top_play['maxcombo']}")
    else:
        print("error lol")

if __name__ == "__main__":
    main()

