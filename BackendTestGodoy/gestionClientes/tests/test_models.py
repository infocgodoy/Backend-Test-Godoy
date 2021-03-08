from mixer.backend.django import mixer
import pytest
#trate de hacer unos pocos testing en pos del tiempo, algunos eran de prueba, otros mas funcionales como este que van directo a la BD
@pytest.mark.django_db
class TestModels:

    def test_platos_precio_mayor_a_cero(self):
        plato = mixer.blend('gestionClientes.Platos', precio=990)
        assert plato.precio_mayor_a_cero == True

    def test_platos_precio_cero(self):
        plato = mixer.blend('gestionClientes.Platos', precio=0)
        assert plato.precio_mayor_a_cero == False
        