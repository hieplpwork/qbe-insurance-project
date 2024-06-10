import unittest
import json
from qbe import app

class FlaskTestCase(unittest.TestCase):
    
    def setUp(self):
        # Creates a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_validate_success(self):
        # Test for a successful validation
        input_data = {
            "data": [
                {"var_name": "country", "category": "UK"},
                {"var_name": "age_group", "category": "18-30"}
            ]
        }
        response = self.app.post('/validate', 
                                 data=json.dumps(input_data), 
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Validation successful', response.data)

    def test_validate_failure(self):
        # Test for a validation failure
        input_data = {
            "data": [
                {"var_name": "country", "category": "Unknown"},
                {"var_name": "unknown_var", "category": "18-25"}
            ]
        }
        response = self.app.post('/validate', 
                                 data=json.dumps(input_data), 
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Invalid category for country: Unknown', response.data)
        self.assertIn(b'Invalid var_name: unknown_var', response.data)

    def test_get_factors_success(self):
        # Test for getting factors successfully
        input_data = {
            "data": [
                {"var_name": "country", "category": "UK"},
                {"var_name": "age_group", "category": "18-30"}
            ]
        }
        response = self.app.post('/get_factors', 
                                 data=json.dumps(input_data), 
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
        response_data = json.loads(response.data.decode('utf-8'))
        expected_results = [
            {"var_name": "country", "category": "UK", "factor": 0.25},
            {"var_name": "age_group", "category": "18-30", "factor": 0.33}
        ]
        self.assertEqual(response_data["results"], expected_results)

    def test_get_factors_partial_country(self):
        # Test for partial success in getting factors
        input_data = {
            "data": [
                {"var_name": "country", "category": "UK"},
                {"var_name": "age_group", "category": "Unknown"}
            ]
        }
        response = self.app.post('/get_factors', 
                                 data=json.dumps(input_data), 
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
        response_data = json.loads(response.data.decode('utf-8'))
        expected_results = [
            {"var_name": "country", "category": "UK", "factor": 0.25}
        ]
        self.assertEqual(response_data["results"], expected_results)

    def test_get_factors_partial_age_group(self):
        # Test for partial success in getting factors
        input_data = {
            "data": [
                {"var_name": "country", "category": "Unknown"},
                {"var_name": "age_group", "category": "50+"}
            ]
        }
        response = self.app.post('/get_factors', 
                                 data=json.dumps(input_data), 
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        
        response_data = json.loads(response.data.decode('utf-8'))
        expected_results = [
             {"var_name": "age_group", "category": "50+", "factor": 0.34}
        ]
        self.assertEqual(response_data["results"], expected_results)
        
if __name__ == '__main__':
    unittest.main()
