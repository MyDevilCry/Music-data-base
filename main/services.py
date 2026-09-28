import requests
import wikipedia
from ytmusicapi import YTMusic


from artists.models import Artists, Release, Track


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


def fetch_and_save_artist_data(artist_id):
    try:
        artist = Artists.objects.get(id=artist_id)
    except Artists.DoesNotExist:
        return False

    if getattr(artist, 'is_fetched', False):
        return True

    wikipedia.set_lang('en')

    search_queries = [
        artist.name,
        f"{artist.name} (band)",
        f"{artist.name} band"
    ]

    for query in search_queries:
        try:
            search_results = wikipedia.search(query)
            if not search_results:
                continue

            for page_title in search_results[:3]:  # Перевіряємо перші 3 результати
                try:
                    summary_text = wikipedia.summary(page_title, sentences=5, auto_suggest=False)

                    # Відсіюємо сторінки неоднозначності
                    if "may refer to" not in summary_text.lower():
                        artist.description = summary_text
                        artist.is_fetched = True
                        artist.save()
                        return True
                except (wikipedia.DisambiguationError, wikipedia.PageError):
                    continue  # Якщо ця конкретна сторінка не підійшла — пробуємо наступну
        except Exception as e:
            print(f"Error searching Wikipedia for query '{query}': {e}")

    return False




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

    except requests.RequestException as e:
        print(f" Error : {e}")

    return ""




