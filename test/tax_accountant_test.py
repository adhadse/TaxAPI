import logging

from app import app
import unittest


class TaxAccountantTest(unittest.TestCase):
  # Check for response 200
  def test_valid_post_method(self):
    tester = app.test_client(self)  # tester object
    response = tester.post("/api/taxAccountant", json={
      "username": "adhadse_example",
      "email": "hello@gmail.com",
      "password": "password is completely correct"
    })
    statuscode = response.status_code
    self.assertEqual(200, statuscode)
    tx_acc_response = tester.get(f"/api/taxAccountant", query_string={
      "username": "adhadse_example",
    })
    tester.delete(f"/api/taxAccountant", query_string={
      'id': tx_acc_response.json['response']['id']
    })

  # check if the content return is application JSON
  def test_index_content(self):
    tester = app.test_client(self)
    tester.post("/api/taxAccountant", json={
      "username": "adhadse_example",
      "email": "hello@gmail.com",
      "password": "password is completely correct"
    })
    tx_acc_response = tester.get("/api/taxAccountant", query_string={
      'username': 'adhadse_example'
    })

    response = tester.get(f"/api/taxAccountant", query_string={
      'id': tx_acc_response.json['response']['id']
    })
    self.assertEqual(response.content_type, "application/json")
    tester.delete(f"/api/taxAccountant", query_string={
      'id': tx_acc_response.json['response']['id']
    })

  # check the Data returned
  def test_get_method(self):
    tester = app.test_client(self)
    tester.post("/api/taxAccountant", json={
      "username": "adhadse_example",
      "email": "hello@gmail.com",
      "password": "password is completely correct"
    })
    tx_acc_response = tester.get("/api/taxAccountant", query_string={
      'username': 'adhadse_example'
    })

    log = logging.getLogger("TaxPayerTest.test_index_content")
    log.debug("response = %s", tx_acc_response.json)

    response = tester.get(f"/api/taxAccountant", query_string={
      'id': tx_acc_response.json['response']['id']
    })
    self.assertEqual(200, response.status_code)
    tester.delete(f"/api/taxAccountant", query_string={
      'id': tx_acc_response.json['response']['id']
    })

  def test_delete_method(self):
    tester = app.test_client(self)
    tester.post("/api/taxAccountant", json={
      "username": "adhadse_example",
      "email": "hello@gmail.com",
      "password": "password is completely correct"
    })
    tx_acc_response = tester.get("/api/taxAccountant", query_string={
      'username': 'adhadse_example'
    })
    response = tester.delete(f"/api/taxAccountant", query_string={
      'id': tx_acc_response.json['response']['id']
    })
    self.assertEqual(response.status_code, 204)
    tester.delete(f"/api/taxAccountant", query_string={
      'id': tx_acc_response.json['response']['id']
    })
