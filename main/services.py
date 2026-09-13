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


