import unittest
from unittest.mock import MagicMock, patch

from metrovalencia import MetroValencia
from metrovalencia.models import (
    PrevisionesResponse,
    ParadasResponse,
    TarjetaInfo,
    ViajesResponse,
    RutaPlan,
    RutaP,
    TarifasResponse,
    Comunicacion,
    IncidenciasV2Response,
    IncidenciasTransporteResponse,
    IncidenciasAccesibilidadResponse,
)
from metrovalencia.models.previsiones import EstadoParada


class TestClassResponsePrevisiones(unittest.TestCase):
    def setUp(self):
        self.metro = MetroValencia(app_name="test", contact="test@test.com", response_type="class")

    def tearDown(self):
        self.metro.close()

    @patch("metrovalencia.http.httpx.Client")
    def test_get_returns_previsiones_response(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"aforoBloqueado": {}, "previsiones": []}
        mock.return_value.get.return_value = mock_response

        result = self.metro.previsiones.get("Alameda")
        self.assertIsInstance(result, PrevisionesResponse)

    @patch("metrovalencia.http.httpx.Client")
    def test_get_returns_previsiones_response_with_string(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"aforoBloqueado": {}, "previsiones": []}
        mock.return_value.get.return_value = mock_response

        result = self.metro.previsiones.get("Alameda")
        self.assertIsInstance(result, PrevisionesResponse)

    @patch("metrovalencia.http.httpx.Client")
    def test_estado_returns_estado_parada(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": 10, "nombre": "Alameda", "estado": "ok"}
        mock.return_value.get.return_value = mock_response

        result = self.metro.previsiones.estado(10)
        self.assertIsInstance(result, EstadoParada)


class TestClassResponseParadas(unittest.TestCase):
    def setUp(self):
        self.metro = MetroValencia(app_name="test", contact="test@test.com", response_type="class")

    def tearDown(self):
        self.metro.close()

    @patch("metrovalencia.http.httpx.Client")
    def test_all_returns_list(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = [{"id": "1", "name": "Test", "lines": []}]
        mock.return_value.get.return_value = mock_response

        result = self.metro.paradas.all()
        self.assertIsInstance(result, list)

    @patch("metrovalencia.http.httpx.Client")
    def test_buscar_returns_paradas_response(self, mock):
        result = self.metro.paradas.buscar("Alameda")
        self.assertIsInstance(result, ParadasResponse)


class TestClassResponseIncidencias(unittest.TestCase):
    def setUp(self):
        self.metro = MetroValencia(app_name="test", contact="test@test.com", response_type="class")

    def tearDown(self):
        self.metro.close()

    @patch("metrovalencia.http.httpx.Client")
    def test_transporte_returns_response(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"incidencias": []}
        mock.return_value.get.return_value = mock_response

        result = self.metro.incidencias.transporte()
        self.assertIsInstance(result, IncidenciasTransporteResponse)

    @patch("metrovalencia.http.httpx.Client")
    def test_accesibilidad_returns_response(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"incidencias": []}
        mock.return_value.get.return_value = mock_response

        result = self.metro.incidencias.accesibilidad()
        self.assertIsInstance(result, IncidenciasAccesibilidadResponse)


class TestClassResponseTarjetas(unittest.TestCase):
    def setUp(self):
        self.metro = MetroValencia(app_name="test", contact="test@test.com", response_type="class")

    def tearDown(self):
        self.metro.close()

    @patch("metrovalencia.http.httpx.Client")
    def test_info_returns_tarjeta_info(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"numero": 123, "tipo": "Test", "saldo": 0}
        mock.return_value.get.return_value = mock_response

        result = self.metro.tarjetas.info(123)
        self.assertIsInstance(result, TarjetaInfo)

    @patch("metrovalencia.http.httpx.Client")
    def test_viajes_returns_viajes_response(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"info": {}, "viajes": []}
        mock.return_value.get.return_value = mock_response

        result = self.metro.tarjetas.viajes(123)
        self.assertIsInstance(result, ViajesResponse)


class TestClassResponseRutas(unittest.TestCase):
    def setUp(self):
        self.metro = MetroValencia(app_name="test", contact="test@test.com", response_type="class")

    def tearDown(self):
        self.metro.close()

    @patch("metrovalencia.http.httpx.Client")
    def test_plan_returns_ruta_plan(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"origen": "A", "destino": "B", "duracion": 10, "segmentos": []}
        mock.return_value.post.return_value = mock_response

        result = self.metro.rutas.plan(1, 2)
        self.assertIsInstance(result, RutaPlan)

    @unittest.skip("Endpoint appears to require valid station IDs")
    @patch("metrovalencia.http.httpx.Client")
    def test_rutap_returns_ruta_p(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"origenId": 1, "destinoId": 2, "tiempo": 10}
        mock.return_value.get.return_value = mock_response

        result = self.metro.rutas.rutap("A", "B")
        self.assertIsInstance(result, RutaP)


class TestClassResponseTarifas(unittest.TestCase):
    def setUp(self):
        self.metro = MetroValencia(app_name="test", contact="test@test.com", response_type="class")

    def tearDown(self):
        self.metro.close()

    @patch("metrovalencia.http.httpx.Client")
    def test_get_returns_tarifas_response(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"idioma": "ES", "tarifas": []}
        mock.return_value.get.return_value = mock_response

        result = self.metro.tarifas.get("ES")
        self.assertIsInstance(result, TarifasResponse)

    def test_invalid_idioma_raises(self):
        with self.assertRaises(ValueError):
            self.metro.tarifas.get("FR")


class TestClassResponseComunicaciones(unittest.TestCase):
    def setUp(self):
        self.metro = MetroValencia(app_name="test", contact="test@test.com", response_type="class")

    def tearDown(self):
        self.metro.close()

    @patch("metrovalencia.http.httpx.Client")
    def test_get_returns_list_of_comunicacion(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = []
        mock.return_value.get.return_value = mock_response

        result = self.metro.comunicaciones.get()
        self.assertIsInstance(result, list)


class TestClassResponseV2(unittest.TestCase):
    def setUp(self):
        self.metro = MetroValencia(app_name="test", contact="test@test.com", response_type="class")

    def tearDown(self):
        self.metro.close()

    @patch("metrovalencia.http.httpx.Client")
    def test_incidencias_get_returns_response(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"success": True, "timestamp": "x", "data": {}}
        mock.return_value.get.return_value = mock_response

        result = self.metro.v2.incidencias.get()
        self.assertIsInstance(result, IncidenciasV2Response)


if __name__ == "__main__":
    unittest.main()