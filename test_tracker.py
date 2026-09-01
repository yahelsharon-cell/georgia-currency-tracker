# 1. Import the function we want to test
from tracker import build_api_url

# 2. Write a test function starting with "test_"
def test_build_api_url():
    # Arrange: Set up dummy data
    dummy_key = "12345"
    base_curr = "USD"
    
    # Act: Run the function
    result = build_api_url(dummy_key, base_curr)
    
    # Assert: Verify the result is exactly what we expect
    expected_url = "https://v6.exchangerate-api.com/v6/12345/latest/USD"
    assert result == expected_url
