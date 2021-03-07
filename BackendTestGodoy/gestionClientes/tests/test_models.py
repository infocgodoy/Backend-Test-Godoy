from mixer.backend.django import mixer
import pytest

@pytest.mark.django_db
class TestModels:

    def test_platos_precio_mayor_a_cero(self):
        plato = mixer.blend('gestionClientes.Platos', precio=990)
        assert plato.precio_mayor_a_cero == True

    def test_platos_precio_cero(self):
        plato = mixer.blend('gestionClientes.Platos', precio=0)
        assert plato.precio_mayor_a_cero == False
        