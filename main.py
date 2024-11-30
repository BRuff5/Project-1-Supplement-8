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
    
def get_postman_token_and_ip():
    """Sends request to https://echo.free.beeceptor.com and extracts Postman-Token and IP address.
    Returns:
        tuple: A tuple containing the Postman-Token and IP address.
    """
    url = "https://echo.free.beeceptor.com"
    status_code, response = get_request(url)
    postman_token = response.get("headers", {}).get("Postman-Token")
    ip_address = response.get("headers", {}).get("X-Forwarded-For") or response.get("origin")
    return postman_token, ip_address

def test_get_request():
    url = "https://httpbin.org/get"
    status_code, response = get_request(url)
    assert status_code == 200, f"Expected 200, got {status_code}"
    assert isinstance(response, dict), f"Expected dict, got {type(response)}"
    print("Passed!")
    
def test_get_postman_token_and_ip():
    token, ip = get_postman_token_and_ip()
    assert token is not None, "Postman-Token should not be None"
    assert ip is not None, "IP address should not be None"
    print("GET Postman-Token and IP test passed!")

if __name__ == "__main__":
    test_get_request()
    test_get_postman_token_and_ip()