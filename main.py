import http.client
import json

def get_request(url: str):
    """Sends an HTTP GET request using http.client."""
    try:
        conn = http.client.HTTPSConnection(url.split('/')[2])  # Extract the hostname
        conn.request("GET", url[url.find('/', 8):])  # Extract the path
        response = conn.getresponse()
        status_code = response.status
        content_type = response.getheader("Content-Type")
        response_text = response.read().decode("utf-8")
        
        if 400 <= status_code <= 499:
            raise Exception(f"Client Error: {status_code}, {response_text}")
        
        if content_type.startswith("application/json"):
            return status_code, json.loads(response_text)
        return status_code, response_text
    except Exception as e:
        raise Exception(f"Error occurred during GET request: {str(e)}")

def send_post_request():
    """Sends an HTTP POST request using http.client."""
    url = "https://echo.free.beeceptor.com"
    payload = {"hello": "world"}
    headers = {"Content-Type": "application/json"}
    
    conn = http.client.HTTPSConnection(url.split('/')[2])  # Extract the hostname
    conn.request("POST", url[url.find('/', 8):], body=json.dumps(payload), headers=headers)
    response = conn.getresponse()
    status_code = response.status
    content_type = response.getheader("Content-Type")
    response_text = response.read().decode("utf-8")
    
    if content_type.startswith("application/json"):
        return status_code, json.loads(response_text)
    return status_code, response_text

import urllib.request
import json

def get_request(url: str):
    """Sends an HTTP GET request using urllib."""
    try:
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req) as response:
            status_code = response.getcode()
            content_type = response.headers.get("Content-Type")
            response_text = response.read().decode("utf-8")
            
            if 400 <= status_code <= 499:
                raise Exception(f"Client Error: {status_code}, {response_text}")
            
            if content_type.startswith("application/json"):
                return status_code, json.loads(response_text)
            return status_code, response_text
    except Exception as e:
        raise Exception(f"Error occurred during GET request: {str(e)}")

def send_post_request():
    """Sends an HTTP POST request using urllib."""
    url = "https://echo.free.beeceptor.com"
    payload = json.dumps({"hello": "world"}).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    
    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as response:
            status_code = response.getcode()
            content_type = response.headers.get("Content-Type")
            response_text = response.read().decode("utf-8")
            
            if content_type.startswith("application/json"):
                return status_code, json.loads(response_text)
            return status_code, response_text
    except Exception as e:
        raise Exception(f"Error occurred during POST request: {str(e)}")
    
    
if __name__ == "__main__":
    # Test the GET request
    status_code, response = get_request("https://httpbin.org/get")
    print(f"GET Response Status: {status_code}")
    print(f"GET Response Body: {response}")

    # Test the POST request
    status_code, response = send_post_request()
    print(f"POST Response Status: {status_code}")
    print(f"POST Response Body: {response}")