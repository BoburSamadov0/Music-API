from rest_framework import serializers
from .models import Song, Album, Artist
from rest_framework.exceptions import ValidationError


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    # album = AlbumSerializer(required=False)

    class Meta:
        model = Song
        fields = '__all__'

    def validate_source(self, value):
        if not value.endswith(".mp3"):
            raise ValidationError("It should end with .mp3")
        return value
