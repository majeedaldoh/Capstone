import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie


class CapstoneTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        
        #self.database_name = "capstoneproject"
        #self.database_path = "postgresql://{}@{}/{}".format('root:Pp251100', 'localhost:5432', self.database_name)
        self.database_path = os.environ['DATABASE_URL']
        if database_path.startswith("postgres://"):
            database_path = database_path.replace(
                "postgres://", "postgresql://", 1)
        
        setup_db(self.app, self.database_path)

        self.casting_assistant_header = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJraUxMSC1xNWxVdDFtcy1IempHbCJ9.eyJpc3MiOiJodHRwczovL21hamVlZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjNkMmM4ZTlhNjE0MWM0NWUwYzVjODUzIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2NzQ5MDU3ODAsImV4cCI6MTY3NDkxMjk4MCwiYXpwIjoiVU5Wd0VnUERhdVJQYnFrRUZhU1I0blRrSFRBRmFCenMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.UAiwcVQrJzDNXuiIf7KmyN1z5MFdCIkKW0WcbJs5Y6djZXP4KDMx61oqNyvtarJ9K14GmuoklyU46_VdXOOJ7Uif6jKQe4WQrCdnuFZSqRjI8W-eOqEFFV7XKrChBRtCTospFSJsDXYI0gwHS3hEIS7q97B8IXazEju9KvI5oTzrQzLe7GGw3o6Z9Hgo6wfje1f3APcuchKug-2XOlBDrM76DRWPCzgQMBvVtaMD0fTSiAqLn0DrJl29QOztHhB73jztRt3bvaQGFGtRvm1t4XsI2P9EarTpuE-mTvlI6wByJsa0zsNt_XoqaFBFjcbizk88RoQIsGqNVKmrnwjp6w'
        }

        self.casting_director_header = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJraUxMSC1xNWxVdDFtcy1IempHbCJ9.eyJpc3MiOiJodHRwczovL21hamVlZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjNkMmM5YWJhNjE0MWM0NWUwYzVjODU5IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2NzQ5MDU5NDQsImV4cCI6MTY3NDkxMzE0NCwiYXpwIjoiVU5Wd0VnUERhdVJQYnFrRUZhU1I0blRrSFRBRmFCenMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.rNuIToco6BFOD8JQx-bsnzIV8QtbyuXO9AjUb9NXYGvkEBLS8dZVE2pmxNnN83zsoBs0waxdTeAA1aL83O93RiZr9g78vm-jeWYlWkZbdwiipNNrpqr96sGV9deMh2nIm_UenUXAUI1V6oHthLNwXjHSszCXfoEEVmeQacdojlXuCb6N0osGmMUkTtcN2Md7G3TjU_UC8R1aS4VgiFT-tqTBDtlGjmoUt3Lrd0oSD3SoCOJyYJeiv4sWNWRQkjJfE5gRThRbWyi3LJoRvEq6jDs2pINbggqjzIOyrFU_xD7jvglfrYt0V_QNayzJmfFtanNmg759y3bt_EDmPKnkMg'
        }

        self.executive_producer_header = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJraUxMSC1xNWxVdDFtcy1IempHbCJ9.eyJpc3MiOiJodHRwczovL21hamVlZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjNkMmM5Njg4NWQ5OTViODdhN2E2MzgzIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2NzQ5MDQ0MzYsImV4cCI6MTY3NDkxMTYzNiwiYXpwIjoiVU5Wd0VnUERhdVJQYnFrRUZhU1I0blRrSFRBRmFCenMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.k0OWB3aENW3nQkzmpfO96H7N5QRlgpVR7c1GW5KCSgwCPV-V5I7t-skslMDARFpGvt2O-uN9zi5uWYit7cX_HoImyJQ1uyr-g7UbZKprZ6F6SAcuMWzMK9-4FkzxoW-RQha0WYl8azfnPZTCQOHRpU2JiT34OYMt1N1yexnWJqBaS6AIxtuquXu_R1_h74ysEqqCIwINWMXmNLcLnYVEYn5uZisINz529bfH07p7FokYX9C1zJqwKoDnEpXSejPI3ODGFJt1egH5n309c0O8qrSasXICj8-Mzmt-Ni6LkQJ26O6Nz9Hn7R3eITv531ZhAW5U-QPfv-ngeJj11FNPJA'
        }
        

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        pass

# test to get actors
    def test_get_actors(self):  
        res = self.client().get('/actors', headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['actors']))

    def test_404_get_actors(self): 
        res = self.client().get('/actors/', headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

# Test to get movies
    def test_get_movies(self):
        res = self.client().get('/movies', headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['movies']))

    def test_404_get_movies(self):
        res = self.client().get('/movies/', headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

# Test to post new actor
    def test_post_actors(self):
        new_test_actor = {
            "name": "Majeed",
            "age": 22,
            "gender": "Male"
        }
        res = self.client().post('/actors', json=new_test_actor, headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_actor'])

    def test_422_post_actors(self):
        new_test_actor = {
            "name": "Majeed",
            "age": "twntee two",
            "gender": "Male"
        }
        res = self.client().post('/actors', json=new_test_actor, headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

# Test to post new movie
    def test_post_movies(self):
        new_test_movie = {
            "title": "FSND",
            "release_date": "2023-01-26"
        }
        res = self.client().post('/movies', json=new_test_movie, headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_movie'])

    def test_422_post_movies(self):
        new_test_movie = {
            "title": "FSND",
            "release_date": "date"
        }
        res = self.client().post('/movies', json=new_test_movie, headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

# Test to delete actor
    def test_delete_actors(self):

        res = self.client().delete('/actors/2', headers=self.executive_producer_header)
        data = json.loads(res.data)
        actor = Actor.query.filter(Actor.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_id'], 2)
        self.assertEqual(actor, None)

    def test_404_delete_actors(self):

        res = self.client().delete('/actors/100', headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

# Test to delete movie
    def test_delete_movies(self):

        res = self.client().delete('/movies/2', headers=self.executive_producer_header)
        data = json.loads(res.data)
        movie = Movie.query.filter(Movie.id == 2).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted_id'], 2)
        self.assertEqual(movie, None)

    def test_404_delete_movies(self):

        res = self.client().delete('/movies/100', headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

# Test to patch actor
    def test_patch_actors(self):

        res = self.client().patch('/actors/3', json={'age': "33"}, headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated_actor'])

    def test_404_patch_actors(self):

        res = self.client().delete('/actors/100', json={'name': "Ali"}, headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

# Test to patch movie
    def test_patch_movies(self):

        res = self.client().patch('/movies/3', json={'title': "New Movie"}, headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated_movie'])

    def test_404_patch_movies(self):  # Test for error behavior

        res = self.client().delete('/movies/100', json={'title': "New Movie"}, headers=self.executive_producer_header)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

# Test RBAC for casting assistant role

    # Test for authorized access
    def test_get_actors_casting_assistant_role(self):
        res = self.client().get('/actors', headers=self.casting_assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['actors']))

    # Test for unauthorized access
    def test_401_get_actors_casting_assistant_role(self):
        res = self.client().get('/actors')

        self.assertEqual(res.status_code, 401)

# Test RBAC for casting director role

    # Test for authorized access
    def test_get_actors_casting_director_role(self):
        res = self.client().get('/actors', headers=self.casting_director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['actors'])

    # Test for unauthorized access
    def test_401_get_actors_casting_director_role(self):
        res = self.client().post('/movies')

        self.assertEqual(res.status_code, 401)

# Test RBAC for executive producer role

    # Test for authorized access
    def test_post_actors_executive_producer_role(self):
        new_test_movie = {
            "title": "movie test name",
            "release_date": "2000-12-12"
        }
        res = self.client().post('/movies', json=new_test_movie, headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_movie'])

    # Test for unauthorized access
    def test_401_get_actors_executive_producer_role(self):
        new_test_movie = {
            "title": "movie test name",
            "release_date": "2000-12-12"
        }
        res = self.client().post('/movies', json=new_test_movie)
        self.assertEqual(res.status_code, 401)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()