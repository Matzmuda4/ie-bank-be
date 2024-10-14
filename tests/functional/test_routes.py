from iebank_api import app
import pytest

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid and contains accounts
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200
    assert isinstance(response.json['accounts'], list)

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is 404
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid and the account is created
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'Finland'})
    assert response.status_code == 200
    assert 'id' in response.json
    assert response.json['name'] == 'John Doe'
    assert response.json['country'] == 'Finland'

def test_update_account(testing_client):
    """
    GIVEN a Flask application
    WHEN an existing account is updated (PUT)
    THEN check the response is valid and the account is updated
    """
    response = testing_client.post('/accounts', json={'name': 'Jane Doe', 'currency': '$', 'country': 'USA'})
    account_id = response.json['id']
    
    update_response = testing_client.put(f'/accounts/{account_id}', json={'name': 'Jane Smith'})
    assert update_response.status_code == 200
    assert update_response.json['name'] == 'Jane Smith'

def test_delete_account(testing_client):
    """
    GIVEN a Flask application
    WHEN an account is deleted (DELETE)
    THEN check the response is valid and the account is deleted
    """
    response = testing_client.post('/accounts', json={'name': 'Mark Lee', 'currency': '€', 'country': 'Germany'})
    account_id = response.json['id']
    
    delete_response = testing_client.delete(f'/accounts/{account_id}')
    assert delete_response.status_code == 200


def test_get_single_account(testing_client):
    """
    GIVEN a Flask application
    WHEN an account is retrieved (GET) on '/accounts/<id>'
    THEN check the response is valid and contains the correct data
    """
    # Create an account first
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'Finland'})
    data = response.get_json()
    account_id = data['id']

    # Retrieve the account by ID
    response = testing_client.get(f'/accounts/{account_id}')
    assert response.status_code == 200
    retrieved_data = response.get_json()

    # Verify the retrieved data matches the created account
    assert retrieved_data['id'] == account_id
    assert retrieved_data['name'] == 'John Doe'
    assert retrieved_data['currency'] == '€'
    assert retrieved_data['country'] == 'Finland'
