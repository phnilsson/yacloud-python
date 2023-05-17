import unittest
from app import app, get_training_log
from flask import url_for
# from app import app

class TestGetTrainingLog(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_route(self):
        response = self.client.get('/api/getTrainingLog')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()