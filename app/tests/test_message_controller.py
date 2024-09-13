import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, AsyncMock
from app.main import app
from app.dtos.message_dto import MessageDTO
from app.utils.exceptions import NotificationFailedException

client = TestClient(app)

@pytest.fixture
def message_data():
    return {"category": "Finances","body": "This is a test notification"}

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() ==  {"message": "Notification app API"}

@pytest.mark.asyncio
@patch("app.services.message_service.MessageService.send_notification", new_callable=AsyncMock)
async def test_send_message_success(mock_send_notification):
    mock_send_notification.return_value = True

    response = client.post("/api/send-notification/", json={
        "category": "Finances",
        "body": "This is a test notification"
    })
    assert response.status_code == 200
    assert response.json() == {"status": "success", "detail": "Notification sent successfully"}

@pytest.mark.asyncio
@patch("app.services.message_service.MessageService.send_notification", new_callable=AsyncMock)
async def test_send_message_failure(mock_send_notification, message_data):
    mock_send_notification.return_value = False

    response = client.post("/api/send-notification/", json=message_data)
    print("la vainita 2",response)
    assert response.status_code == 500
    assert response.json() == {"detail": "Failed to send notification"}

@pytest.mark.asyncio
@patch("app.services.message_service.MessageService.send_notification", new_callable=AsyncMock)
async def test_send_message_invalid_data(mock_send_notification):
    invalid_data = {
        "category": "Test Category"
        # Missing body field
    }

    response = client.post("/api/send-notification/", json=invalid_data)
    assert response.status_code == 422  # Unprocessable Entity due to validation error