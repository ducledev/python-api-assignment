import falcon
import json
from falcon import testing
from customer.app import app
from urllib.parse import urlencode


class MyTestCase(testing.TestCase):
    def setUp(self):
        super(MyTestCase, self).setUp()
        self.app = app

        self.headers = {
            "Accept": "application/json", "Content-Type": "application/json",
            "Authorization": "JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
                             ".eyJ1c2VybmFtZSI6ImdpZ2EiLCJwYXNzd29yZCI6ImdpZ2EiLCJleHAiOjE2MTA3NzU4Njl9.Q4KfxBSzQ"
                             "-Yxw7871elUQjVh7thgZyw_CCGX5z4sUGQ"
        }


class TestAuth(MyTestCase):
    def test_home(self):
        response = self.simulate_get('/')
        assert response.status == falcon.HTTP_200

    def test_a_customer(self):
        response = self.simulate_get('/customers/1')
        assert response.status == falcon.HTTP_401

    def test_list_customer(self):
        response = self.simulate_get('/customers')
        assert response.status == falcon.HTTP_401

    def test_create_customer(self):
        response = self.simulate_post('/customers')
        assert response.status == falcon.HTTP_401

    def test_update_customer(self):
        response = self.simulate_put('/customers')
        assert response.status == falcon.HTTP_401

    def test_delete_customer(self):
        response = self.simulate_delete('/customers/1')
        assert response.status == falcon.HTTP_401


class TestMyAppWithAuth(MyTestCase):
    def test_a_customer(self):
        response = self.simulate_get('/customers/1', headers=self.headers)
        assert response.status == falcon.HTTP_200
        assert response.json.get('customer').get('id') == 1

    def test_list_customer(self):
        response = self.simulate_get('/customers', headers=self.headers)
        assert response.status == falcon.HTTP_200
        customers = response.json.get('customers', [])
        assert len(customers) > 0
