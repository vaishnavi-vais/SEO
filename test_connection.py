import requests
import ssl
import certifi

def test_connection():
    try:
        # Test connection to Grok API
        session = requests.Session()
        session.verify = certifi.where()
        
        # Try to make a simple HEAD request
        response = session.head('https://api.grok.ai', timeout=10)
        print(f"Connection successful! Status code: {response.status_code}")
        return True
    except Exception as e:
        print(f"Connection failed. Error: {str(e)}")
        return False

if __name__ == "__main__":
    test_connection()
