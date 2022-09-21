import logging

from app import app
import unittest


unittest.TestLoader.sortTestMethodsUsing = None


class CountryAndStateTest(unittest.TestCase):
  # Check for response 200
  def test_1_country_valid_post_method(self):
    tester = app.test_client(self)  # tester object
    response = tester.post("/api/country", json={
      "name": "ind",
      "central_tax": 5
    })
    statuscode = response.status_code
    self.assertEqual(200, statuscode)
    c_response = tester.get(f"/api/country", query_string={
      'name': 'ind'
    })
    tester.delete(f"/api/country", query_string={
      'id': c_response.json['response']['id']
    })

  # check the Data returned
  def test_2_country_get_method(self):
    tester = app.test_client(self)

    # First post the data
    tester.post("/api/country", json={
      "name": "ind",
      "central_tax": 5
    })
    c_response = tester.get("/api/country", query_string={
      'name': 'ind'
    })
    self.assertEqual(200, c_response.status_code)
    tester.delete(f"/api/country", query_string={
      'id': c_response.json['response']['id']
    })

  def test_3_state_valid_post_method(self):
    tester = app.test_client(self)
    # First post country
    tester.post("/api/country", json={
      "name": "ind",
      "central_tax": 5
    })
    # access country idx
    c_response = tester.get("/api/country", query_string={
      'name': 'ind'
    })
    response = tester.post("/api/state", json={
      "name": "mp",
      "state_tax": 2,
      "country": c_response.json['response']['id']
    })
    self.assertEqual(200, response.status_code)
    s_response = tester.get(f"/api/state", query_string={
      'name': 'mp'
    })
    tester.delete(f"/api/state", query_string={
      'id': s_response.json['response']['id']
    })
    tester.delete(f"/api/country", query_string={
      'id': c_response.json['response']['id']
    })

  # check the Data returned
  def test_4_state_get_method(self):
    tester = app.test_client(self)
    # First post country, get idx and then post state
    tester.post("/api/country", json={
      "name": "ind",
      "central_tax": 5
    })
    c_response = tester.get("/api/country", query_string={
      'name': 'ind'
    })
    tester.post("/api/state", json={
      "name": "mp",
      "state_tax": 2,
      "country": c_response.json['response']['id']
    })

    # Check get method
    response = tester.get("/api/state", query_string={
      'name': 'mp'
    })
    self.assertEqual(200, response.status_code)
    tester.delete(f"/api/country", query_string={
      'id': c_response.json['response']['id']
    })
    tester.delete(f"/api/state", query_string={
      'id': response.json['response']['id']
    })

  def test_5_tax_payer_post_method_with_country_and_state(self):
    tester = app.test_client(self)

    # First post country and state
    tester.post("/api/country", json={
      "name": "ind",
      "central_tax": 5
    })
    response = tester.get("/api/country", query_string={
      'name': 'ind'
    })
    tester.post("/api/state", json={
      "name": "mp",
      "state_tax": 2,
      "country": response.json['response']['id']
    })

    s_response = tester.get("/api/state", query_string={
      'name': 'mp'
    })
    c_response = tester.get("/api/country", query_string={
      'name': 'ind'
    })
    response = tester.post("/api/taxPayer", json={
      "username": "adhadse_example",
      "email": "hello@gmail.com",
      "password": "password is completely correct",
      "country": c_response.json['response']['id'],
      "state": s_response.json['response']['id']
    })
    statuscode = response.status_code
    self.assertEqual(200, statuscode)
    tester.delete(f"/api/state", query_string={
      'id': s_response.json['response']['id']
    })
    tester.delete(f"/api/country", query_string={
      'id': c_response.json['response']['id']
    })
    t_py_response = tester.get(f"/api/taxPayer", query_string={
      'username': "adhadse_example"
    })
    tester.delete(f"/api/taxPayer", query_string={
      'id': t_py_response.json['response']['id']
    })


  def test_6_country_delete_method(self):
    tester = app.test_client(self)
    # First post country
    tester.post("/api/country", json={
      "name": "ind",
      "central_tax": 5
    })
    response = tester.get("/api/country", query_string={
      'name': 'ind'
    })
    response = tester.delete(f"/api/country", query_string={
      'id': response.json['response']['id']
    })
    self.assertEqual(204, response.status_code)

  def test_7_state_delete_method(self):
    tester = app.test_client(self)
    # First post state
    tester.post("/api/country", json={
      "name": "ind",
      "central_tax": 5
    })
    # access country idx
    c_response = tester.get("/api/country", query_string={
      'name': 'ind'
    })
    tester.post("/api/state", json={
      "name": "mp",
      "state_tax": 2,
      "country": c_response.json['response']['id']
    })
    response = tester.get("/api/state", query_string={
      'name': 'mp'
    })

    # test delete method of state
    response = tester.delete(f"/api/state", query_string={
      'id': response.json['response']['id']
    })
    self.assertEqual(response.status_code, 204)
    tester.delete(f"/api/country", query_string={
      'id': c_response.json['response']['id']
    })



