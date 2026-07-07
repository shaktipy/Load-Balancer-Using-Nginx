import unittest

from app.app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_api_server_returns_non_unknown_server_id(self):
        response = self.client.get('/api/server')
        self.assertEqual(response.status_code, 200)
        payload = response.get_json()
        self.assertIn('server_id', payload)
        self.assertNotEqual(payload['server_id'], 'Unknown Server')


if __name__ == '__main__':
    unittest.main()
