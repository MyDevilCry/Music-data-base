import requests
from ytmusicapi import YTMusic

from artists.models import Release, Track


def fetch_and_save_album_data(release_id):
    try:
        release = Release.objects.get(id=release_id)
    except Release.DoesNotExist:
        return False

    yt=YTMusic()

    artist_name = release.artists.name if hasattr(release,'artists') else ""
    query = f"{artist_name} {release.release_name}"

    search_results = yt.search(query, filter='albums')
    if not search_results:
        return False

    browse_id = search_results[0]['browseId']
    album_data = yt.get_album(browse_id)

    if album_data.get('description') and not release.release_description:
        release.release_description = album_data['description']
        release.save()

    tracks = album_data.get('tracks',[])
    for index, track_info in enumerate(tracks,start=1):
        Track.objects.update_or_create(
            release=release,
            position=index,
            defaults = {
                'title': track_info.get('title',''),
                'duration':track_info.get('duration',''),

            }
        )
    return True


def get_wikipedia_album_summary(album_name, artist_name, lang='en'):
    user_agent = "MusicDataBaseApp/1.0 (contact@example.com)"
    headers = {'User-Agent':user_agent}
    query= f"{album_name} {artist_name} album"
    search_url = f"https://{lang}.wikipedia.org/w/api.php"
    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json"
    }
    try:
        response = requests.get(search_url, params=search_params, headers=headers).json()
        results = response.get('query',{}).get('search',[])

        if results:
            page_title = results[0]['title']
            summary_url = f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{requests.utils.quote(page_title)}"
            summary_res = requests.get(summary_url, headers=headers).json()

            return summary_res.get('extract', '')

    except Exception as e:
        print(f" Error : {e}")

    return ""




