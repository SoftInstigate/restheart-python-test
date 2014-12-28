# --------------------------------------------------- #
# RESTHeart - Python integration test suite           #
# A set of integration tests showing how to interact  #
# with RESTHeart's API via Python.                    #
# It's more ore less the Python version of:           #
# http://restheart.org/docs/walkthrough.html          #
# --------------------------------------------------- #

__author__ = 'mturatti'

import unittest
import restutils
from config import DATABASE_URL, COLLECTION_URL, HEADERS


class TestBasicRESTHeartIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("+ setUpClass")
        params = {'description': 'This is a test db created with RESTHeart'}
        r = restutils.put_resource(DATABASE_URL,  params=params, headers=HEADERS)
        assert r.status_code == 201

    def setUp(self):
        print("++ setUp")
        params = {'description': 'Test collection'}
        r = restutils.put_resource(COLLECTION_URL, params=params, headers=HEADERS)
        self.assertEquals(r.status_code, 201)

    def test_post_documents(self):
        print("+++ test_post_documents at: " + COLLECTION_URL)

        print("Create a first document")
        r = restutils.post_resource(COLLECTION_URL,
                                    json={'name': 'RESTHeart', 'description': 'Open-source REST API for MongoDB'})
        self.assertEquals(r.status_code, 201)

        print("Create a second document")
        r = restutils.post_resource(COLLECTION_URL,
                                    json={'name': 'MongoDB', 'description': 'Leading open-source document database'})
        self.assertEquals(r.status_code, 201)

        print("Get the collection")
        r = restutils.get_resource(COLLECTION_URL, params=None)
        self.assertEquals(r.status_code, 200)

        print("Assert it contains 2 documents")
        self.assertEquals(2, restutils.count_documents(r))

        print("Get a document by name using collection's filter")
        r = restutils.get_resource(COLLECTION_URL, params={'filter': '{"name": "RESTHeart"}'})
        self.assertEquals(r.status_code, 200)

        print("Assert it contains 1 document")
        self.assertEquals(1, restutils.count_documents(r))

        print("The request's 'text' field contains the whole document:\n" + r.text)

    def tearDown(self):
        r = restutils.delete_resource(COLLECTION_URL)
        self.assertEquals(r.status_code, 204)
        print("++ tearDown")

    @classmethod
    def tearDownClass(cls):
        r = restutils.delete_resource(DATABASE_URL)
        assert r.status_code == 204
        print("+ tearDownClass")


if __name__ == '__main__':
    unittest.main()