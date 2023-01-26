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
        #self.database_path = "postgresql://{}@{}/{}".format('postgres:Pp251100', 'localhost:5432', self.database_name)
        self.database_path = os.environ['DATABASE_URL']
        if database_path.startswith("postgres://"):
            database_path = database_path.replace(
                "postgres://", "postgresql://", 1)
        
        setup_db(self.app, self.database_path)

        self.casting_assistant_header = {
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJraUxMSC1xNWxVdDFtcy1IempHbCJ9.eyJpc3MiOiJodHRwczovL21hamVlZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjNkMmM4ZTlhNjE0MWM0NWUwYzVjODUzIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2NzQ3NTk5NjMsImV4cCI6MTY3NDc2NzE2MywiYXpwIjoiVU5Wd0VnUERhdVJQYnFrRUZhU1I0blRrSFRBRmFCenMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.uj1q48oqLip7x6LOKJ4yd6disrWmQRI-gMCqrc8YiltNGzIh1O_E8ABCk3ItELyBT_1ETyor-vD5Eh1rzwxc9bogkqMwnkoR9RSNlchNNTM6l4rICgVTiGia_cB-M3ut1Ebp21HdzVBpn6itPzp4XKAYFwsSflXahZzvJvuTowfRvGAFzxBrG7fj4ruEUN-fFTUhALxzzXJlSMAqc9lPyWR7OdzH6UcdxVBSfoPNG3hNPHaCiLtFA9NQoPRTe5j6RhQLnEawEjkGrMZbICj_sQZO9seRF20SohMeaPBeQC6spDCrXBLEcXf6MMU6fD2ZoHQPjs0Myl4X6UjDwk1ZSw'
        }

        self.casting_director_header = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJraUxMSC1xNWxVdDFtcy1IempHbCJ9.eyJpc3MiOiJodHRwczovL21hamVlZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjNkMmM5YWJhNjE0MWM0NWUwYzVjODU5IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2NzQ3NTk4MDAsImV4cCI6MTY3NDc2NzAwMCwiYXpwIjoiVU5Wd0VnUERhdVJQYnFrRUZhU1I0blRrSFRBRmFCenMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.lqa4moCWNXaLlyvXM6Rs_hGRG9PAl7yL18azwu8KmkKgHstrWwXh7-GuGuzwLWHFZ1hrKEdLtwF4qhST92sDKuYTplv1BevaCchNp194729YkcnOBYmoS-AK3-quE1nOYuPvwdpKfrvxEMnFQEhY40Mcj1gcy_VPdeYnlUoHUtWBFFZiFAjXeEjNyy8jVil_9fI5si3OZ9K1jcw3HoTbTr5Smn1z63-KmwjM-mtbjHVknc5c1LxLkGB7t8NzKZG7kb3pQZrllHeRti-5KtghYpuBwdT3SZ_t8b6bepX4CMALTvFF9Ru2XL1UkC7YRHFFKE7R5SXqm8NyFrTCD9mFIA'
        }

        self.executive_producer_header = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJraUxMSC1xNWxVdDFtcy1IempHbCJ9.eyJpc3MiOiJodHRwczovL21hamVlZC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjNkMmM5Njg4NWQ5OTViODdhN2E2MzgzIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2NzQ3NTg5NDksImV4cCI6MTY3NDc2NjE0OSwiYXpwIjoiVU5Wd0VnUERhdVJQYnFrRUZhU1I0blRrSFRBRmFCenMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.BHJy1jIV5ZgG_YgDCIubxj0FMv3RN4SL3236Ev3FKzzcVWdWU6e77h2iDxqSFWAnJVTughvv-j0QJHCMbQU9PBguKHJhdqys_BkN_WlL42b-9Xg5oVeQ7Abyf6dHSF56_22Z1ubpy-fxWeXu3VmaxJOxf7T7UW-swArsDBFsBslzt8x0HVL5yzDQQM6Zp3_QRedO952Jq5TxIk9J401WGSYmDLGcYarX7ggdT6dZYM9-SjIRiqeP0yoMXoOriFtpmvlyO8JfffZSr1y7PyuhSbehXBtXadcbjX_eaKsTb-k79VaTNYqKKuijVM9UREzlvjWwHma9iEN9E4vTMBeOEA'
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

        res = self.client().patch('/actors/1', json={'age': "33"}, headers=self.executive_producer_header)
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

        res = self.client().patch('/movies/1', json={'title': "New Movie"}, headers=self.executive_producer_header)
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
        new_test_actor = {
            "name": "actor name test role ",
            "age": 20,
            "gender": "Female"
        }
        res = self.client().post('/actors', json=new_test_actor, headers=self.casting_director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['new_actor'])

    # Test for unauthorized access
    def test_401_get_actors_casting_director_role(self):
        new_test_movie = {
            "title": "movie test name",
            "release_date": "2000-12-12"
        }
        res = self.client().post('/movies', json=new_test_movie, headers=self.casting_director_header)

        self.assertEqual(res.status_code, 401)

# Test RBAC for executive producer role

    # Test for authorized access
    def test_get_actors_executive_producer_role(self):
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