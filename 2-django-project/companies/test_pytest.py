import pytest
import json
from django.urls import reverse


companies_url = reverse("companies-list")

# If it is required to access the database during the test, use django_db mark.
@pytest.mark.django_db
def test_zero_companies_should_return_empty_list(client) -> None:
    # Pytest also allows access to Client class by default!
    response = client.get(companies_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []



# Pytest is EXCPLICIT!!!