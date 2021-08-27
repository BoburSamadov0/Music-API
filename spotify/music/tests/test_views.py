from django.test import TestCase, Client

from music.models import Artist, Album, Song


class TestArtistModelViewSet(TestCase):
    def setUp(self) -> None:
        self.artist = Artist.objects.create(name="Example name")
        self.client = Client()

    def test_get_response(self):
        response = self.client.get('/artists/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], "Example name")
        self.assertEqual(response.data[0]["picture"], "")


class TestSongsModelViewSet(TestCase):
    def setUp(self) -> None:
        self.artist = Artist.objects.create(name="Test Example")
        self.album = Album.objects.create(title="Test Title", artist=self.artist)
        self.song = Song.objects.create(album=self.album, title="Test Song", listened=0)
        self.song = Song.objects.create(album=self.album, title="Test Song 2", listened=0)
        self.client = Client()

    def test_song_search(self):
        response = self.client.get("/songs/?search=Test")
        data = response.data
        self.assertEqual(response.status_code, 200)
        self.assertEquals(data[0]['title'], 'Test Song')
