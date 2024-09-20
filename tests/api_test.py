import pytest
from src.api.app import app

@pytest.fixture
def client():
    return app.test_client()

def test_prediction(client):
    response = client.post('/predict', json={"input_data": [...]})
    assert response.status_code == 200
    assert 'prediction' in response.json