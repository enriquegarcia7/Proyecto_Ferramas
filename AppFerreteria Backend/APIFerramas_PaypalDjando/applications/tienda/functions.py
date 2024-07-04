import base64
import requests


PAYPAL_CLIENT_ID = 'AUxR_B4GyQvxRksgD3lwypzg6NwfhdzXfZbtOM9cy0wUMVvoQ0zW1e1mdrKXOmYIOMQtkgbeP4fHp6lY'
PAYPAL_CLIENT_SECRET = 'EOYoSVYWGAVi5MNvT0yF-NoK77QqXKb3-JQFRCjNvr3sdaxid7TVCewtEQ9W6JEvwuhEkNgOgobqoT__'
BASE_URL = "https://api-m.sandbox.paypal.com"

def generateAccessToken():
    if not PAYPAL_CLIENT_ID or not PAYPAL_CLIENT_SECRET:
        raise ValueError('no existen credenciales')
    
    auth = f"{PAYPAL_CLIENT_ID}:{PAYPAL_CLIENT_SECRET}"
    auth = base64.b64encode(auth.encode()).decode('utf-8')
    
    respose = requests.post(
        "https://api-m.sandbox.paypal.com/v1/oauth2/token",
        data={"grant_type": "client_credentials"},
        headers={"Authorization": f"Basic {auth}"}
    )
    data = respose.json()
    return data['access_token']


def create_order(productos):
    print(productos)
    
    try:
        accsess_token = generateAccessToken()
        url = "https://api-m.sandbox.paypal.com/v2/checkout/orders"
        payload = {
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "amount": {
                        "currency_code": "USD",
                        "value": "5"
                    }
                }
            ]
        }
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {accsess_token}"
        }
        
        response = requests.post(url, headers=headers, json=payload)
        print('--- response ---', response.json())
        return response.json()
    except Exception as error:
        print('*****')
        print(error)


def capture_order(orderID):
    access_token = generateAccessToken()
    url = f"https://api-m.sandbox.paypal.com/v2/checkout/orders/{orderID}/capture"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    
    response = requests.post(url, headers=headers)
    
    return response.json()