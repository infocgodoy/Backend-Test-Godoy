from mixer.backend.django import mixer
import pytest

@pytest.fixture
def plato(request, db):
    return mixer.blend('gestionClientes.Platos', precio=request.param)

@pytest.mark.parametrize('plato', [990], indirect=True)
def test_platos_precio_mayor_a_cero(plato):
    
    assert plato.precio_mayor_a_cero == True

@pytest.mark.parametrize('plato', [0], indirect=True)
def test_platos_precio_cero(plato):
    
    assert plato.precio_mayor_a_cero == False
        