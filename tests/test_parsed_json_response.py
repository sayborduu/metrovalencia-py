import unittest
from unittest.mock import MagicMock, patch

from metrovalencia import MetroValencia


class TestParsedJsonResponsePrevisiones(unittest.TestCase):
    def setUp(self):
        self.metro = MetroValencia(app_name="test", contact="test@test.com", response_type="parsed_json")

    def tearDown(self):
        self.metro.close()

    @patch("metrovalencia.http.httpx.Client")
    def test_get_returns_dict_snake_case(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"aforoBloqueado": {}, "previsiones": []}
        mock.return_value.get.return_value = mock_response

        result = self.metro.previsiones.get("Alameda")
        self.assertIsInstance(result, dict)
        self.assertIn("aforo_bloqueado", result)

    @patch("metrovalencia.http.httpx.Client")
    def test_estado_returns_dict(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": 10, "nombre": "Test"}
        mock.return_value.get.return_value = mock_response

        result = self.metro.previsiones.estado(10)
        self.assertIsInstance(result, dict)


class TestParsedJsonResponseParadas(unittest.TestCase):
    def setUp(self):
        self.metro = MetroValencia(app_name="test", contact="test@test.com", response_type="parsed_json")

    def tearDown(self):
        self.metro.close()

    @patch("metrovalencia.http.httpx.Client")
    def test_all_returns_list(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = [{"id": "1", "name": "Test"}]
        mock.return_value.get.return_value = mock_response

        result = self.metro.paradas.all()
        self.assertIsInstance(result, list)

    @patch("metrovalencia.http.httpx.Client")
    def test_buscar_returns_dict(self, mock):
        result = self.metro.paradas.buscar("Alameda")
        self.assertIsInstance(result, dict)


class TestParsedJsonResponseIncidencias(unittest.TestCase):
    def setUp(self):
        self.metro = MetroValencia(app_name="test", contact="test@test.com", response_type="parsed_json")

    def tearDown(self):
        self.metro.close()

    @patch("metrovalencia.http.httpx.Client")
    def test_transporte_returns_dict(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"incidencias": []}
        mock.return_value.get.return_value = mock_response

        result = self.metro.incidencias.transporte()
        self.assertIsInstance(result, dict)

    @patch("metrovalencia.http.httpx.Client")
    def test_accesibilidad_returns_dict(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"incidencias": []}
        mock.return_value.get.return_value = mock_response

        result = self.metro.incidencias.accesibilidad()
        self.assertIsInstance(result, dict)


class TestParsedJsonResponseTarjetas(unittest.TestCase):
    def setUp(self):
        self.metro = MetroValencia(app_name="test", contact="test@test.com", response_type="parsed_json")

    def tearDown(self):
        self.metro.close()

    @patch("metrovalencia.http.httpx.Client")
    def test_info_returns_dict(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"numero": 123}
        mock.return_value.get.return_value = mock_response

        result = self.metro.tarjetas.info(123)
        self.assertIsInstance(result, dict)

    @patch("metrovalencia.http.httpx.Client")
    def test_viajes_returns_dict(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"info": {}, "viajes": []}
        mock.return_value.get.return_value = mock_response

        result = self.metro.tarjetas.viajes(123)
        self.assertIsInstance(result, dict)


class TestParsedJsonResponseRutas(unittest.TestCase):
    def setUp(self):
        self.metro = MetroValencia(app_name="test", contact="test@test.com", response_type="parsed_json")

    def tearDown(self):
        self.metro.close()

    @patch("metrovalencia.http.httpx.Client")
    def test_plan_returns_dict(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"origen": "A", "duracion": 10}
        mock.return_value.post.return_value = mock_response

        result = self.metro.rutas.plan(1, 2)
        self.assertIsInstance(result, dict)

    @unittest.skip("Endpoint requires valid station IDs")
    @patch("metrovalencia.http.httpx.Client")
    def test_rutap_returns_dict(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"tiempo": 10}
        mock.return_value.get.return_value = mock_response

        result = self.metro.rutas.rutap("A", "B")
        self.assertIsInstance(result, dict)


class TestParsedJsonResponseTarifas(unittest.TestCase):
    def setUp(self):
        self.metro = MetroValencia(app_name="test", contact="test@test.com", response_type="parsed_json")

    def tearDown(self):
        self.metro.close()

    @patch("metrovalencia.http.httpx.Client")
    def test_get_returns_dict(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"idioma": "ES"}
        mock.return_value.get.return_value = mock_response

        result = self.metro.tarifas.get("ES")
        self.assertIsInstance(result, dict)

    def test_invalid_idioma_raises(self):
        with self.assertRaises(ValueError):
            self.metro.tarifas.get("FR")


class TestParsedJsonResponseComunicaciones(unittest.TestCase):
    def setUp(self):
        self.metro = MetroValencia(app_name="test", contact="test@test.com", response_type="parsed_json")

    def tearDown(self):
        self.metro.close()

    @patch("metrovalencia.http.httpx.Client")
    def test_get_returns_list(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = []
        mock.return_value.get.return_value = mock_response

        result = self.metro.comunicaciones.get()
        self.assertIsInstance(result, list)


class TestParsedJsonResponseV2(unittest.TestCase):
    def setUp(self):
        self.metro = MetroValencia(app_name="test", contact="test@test.com", response_type="parsed_json")

    def tearDown(self):
        self.metro.close()

    @patch("metrovalencia.http.httpx.Client")
    def test_incidencias_get_returns_dict(self, mock):
        mock_response = MagicMock()
        mock_response.json.return_value = {"success": True, "data": {}}
        mock.return_value.get.return_value = mock_response

        result = self.metro.v2.incidencias.get()
        self.assertIsInstance(result, dict)


if __name__ == "__main__":
    unittest.main()