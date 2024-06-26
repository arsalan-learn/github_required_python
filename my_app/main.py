import urllib3
from urllib3.connection import HTTPConnection

def main():
    http = urllib3.PoolManager()
    conn = HTTPConnection('jsonplaceholder.typicode.com')

    method = 'GET'
    url = '/todos/1'
    body = None
    headers = {}
    chunked = True

    conn.request_chunked(method, url, body, headers, chunked)
    response = conn.getresponse()
    
    if response.status == 200:
        print("Response from APII:", response.read().decode('utf-8'))
    else:
        print("Failed to get response from API")

if __name__ == "__main__":
    main()