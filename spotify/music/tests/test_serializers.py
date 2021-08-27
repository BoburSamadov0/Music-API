from django.test import TestCase
from music.models import Artist, Album
from music.serializers import ArtistSerializer, SongSerializer


class TestArtistSerializer(TestCase):
    def setUp(self) -> None:
        self.artist = Artist.objects.create(name="Example name")

    def test_data(self):
        data = ArtistSerializer(self.artist).data
        assert data['id'] is not None
        assert data['name'] == "Example name"

        # assert True


class TestSongSerializer(TestCase):
    def setUp(self) -> None:
        self.artist = Artist.objects.create(name="Test Example")
        self.album = Album.objects.create(title="Test Title", artist=self.artist)

    def test_song_is_valid(self):
        data = {"title": "Test song",
                "source": "https://example.com/audio_2.mp3",
                "listened": 0,
                "album": self.album.id}

        serializer = SongSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_song_invalid(self):
        data = {"title": "Test song",
                "source": "https://example.com/audio_2",
                "listened": 0,
                "album": self.album.id}

        serializer = SongSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors["source"][0], 'It should end with .mp3')
