# QBE Insurance Project

## Setup
1. Install Python environment and necessary packages

2. Install Flask to work with APIs

3. Clone the repository
    git clone https://github.com/hieplpwork/qbe-insurance-project.git

## Running the API

1. Start the Flask server
   ```sh
    python qbe.py
   ```
3. The API will be available at `http://127.0.0.1:5000`

## API Endpoints

### POST /validate
Validates the input data.

- **Request Body**
    ```json
    {
        "data": [
            {"var_name": "country", "category": "UK"},
            {"var_name": "age_group", "category": "30-50"}
        ]
    }
    ```

- **Response**
    ```json
    {
        "message": "Validation successful"
    }
    ```

### POST /get_factors
Returns the factors for the input data.

- **Request Body**
    ```json
    {
        "data": [
            {"var_name": "country", "category": "UK"},
            {"var_name": "age_group", "category": "30-50"}
        ]
    }
    ```

- **Response**
    ```json
    {
        "results": [
            {"var_name": "country", "category": "UK", "factor": 0.25},
            {"var_name": "age_group", "category": "30-50", "factor": 0.33}
        ]
    }
    ```

## Running the Tests

1. Test with the Postman app:
### POST /validate
- Create a POST request with the URL: http://127.0.0.1:5000/validate
- Add a Header key and value: Content-Type: application/json
- Add a raw body. For example:
    ```json
    {
        "data": [
            {"var_name": "country", "category": "UK"},
            {"var_name": "age_group", "category": "30-50"}
        ]
    }
    ```
- Click on Send button

### POST /get_factors
- Create a POST request with the URL: http://127.0.0.1:5000/get_factors
- Add a Header key and value: Content-Type: application/json
- Add a raw body. For example:
    ```json
    {
        "data": [
            {"var_name": "country", "category": "UK"},
            {"var_name": "age_group", "category": "30-50"}
        ]
    }
    ```
- Click on Send button

2. Run unit tests
   ```sh
    python unit_test.py
   ```
