import requests

def get_request(url: str):
    """Sends an HTTP GET request to specified URL.
    Parameters:
        url (str): The URL
    Returns:
        tuple: A tuple containing the status code and text
    Raises:
        Exception: If the status code is in the range 400 to 499
    """
    try:
        response = requests.get(url)
        if 400 <= response.status_code <= 499:
            raise Exception(f"Client Error: {response.status_code}, {response.text}")
        if response.headers.get("Content-Type", "").startswith("application/json"):
            return response.status_code, response.json()
        return response.status_code, response.text
    except Exception as e:
        raise Exception(f"Error occurred during GET request: {str(e)}")
    
    

def test_get_request():
    url = "https://httpbin.org/get"
    status_code, response = get_request(url)
    assert status_code == 200, f"Expected 200, got {status_code}"
    assert isinstance(response, dict), f"Expected dict, got {type(response)}"
    print("Passed!")

if __name__ == "__main__":
    test_get_request()