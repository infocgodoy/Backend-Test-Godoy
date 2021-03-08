from django.urls import reverse, resolve

class TestUrls:

    def test_detail_url(self):
        path = reverse('detail', kwargs={'pk': 1})
        assert resolve(path).view_name == 'detail'

def test_hello_word():
    hello = "Hello World"
    assert hello.upper() == "HELLO WORLD"   

def test_suma():

    assert 2 + 2 == 4