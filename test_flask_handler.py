
import unittest
import flask_handler
import requests
import json
import format

# python3 -m unittest -v


class TestUnitTest(unittest.TestCase):
    def test_string(self):
        pass

    def test_post_json(self):
        url = 'http://0.0.0.0:5000/get_json_post'
        headers = {'Authorization': 'Bearer token'}
        jsons = format.TestFormat("client", "hello, client").get_json()
        res = requests.post(url, headers=headers, json=jsons)
        print(res.status_code)
        print(res.text, type(res.text))


if __name__ == '__main__':
    unittest.main()
