from rest_framework import serializers
from artists.models import Artists, Release


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = ('slug','name','image','year_formed')


class ArtistDetailSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Artists
        fields = '__all__'


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ['slug','release_name','release_date','release_image']

class ReleaseDetailSerializer(serializers.ModelSerializer):
    release = serializers.StringRelatedField(many=False, read_only=True)
    class Meta:
        model = Release
        exclude = ['is_yt_fetched']