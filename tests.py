from this import d
import unittest
from server import app


class FlaskTests(unittest.TestCase):
    def setUp(self):
        """Set up client for testing"""
        self.client = app.test_client()
        app.config['TESTING'] = True

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = 1

    def test_ping(self):
        result = self.client.get("/", follow_redirects=True)
        self.assertIn(b"")



if __name__ == "__main__":
    unittest.main()