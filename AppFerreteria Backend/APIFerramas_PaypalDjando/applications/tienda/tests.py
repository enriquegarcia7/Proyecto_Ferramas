from django.test import TestCase
from unittest.mock import patch, MagicMock
from applications.tienda.functions import generateAccessToken

from unittest.mock import patch, MagicMock, ANY
from applications.tienda.functions import create_order

# class TestPaypalConnection(TestCase):
#     @patch('applications.tienda.functions.requests.post')
#     def test_generate_access_token(self, mock_post):
#         # Configura el mock para simular una respuesta exitosa de la API de PayPal
#         mock_response = MagicMock()
#         mock_response.json.return_value = {
#             'access_token': 'fake_access_token'
#         }
#         mock_post.return_value = mock_response

#         # Llama a la función que deseas probar
#         access_token = generateAccessToken()

#         # Verifica que la función devuelva el token de acceso esperado
#         self.assertEqual(access_token, 'fake_access_token')

#         # Verifica que se haya llamado a requests.post con los parámetros correctos
#         mock_post.assert_called_once_with(
#             "https://api-m.sandbox.paypal.com/v1/oauth2/token",
#             data={"grant_type": "client_credentials"},
#             headers={"Authorization": ANY}
#         )



from unittest.mock import patch
from django.test import TestCase
from applications.tienda.functions import create_order  

class TestCreateOrder(TestCase):
    @patch('applications.tienda.functions.generateAccessToken') 
    @patch('requests.post')  
    def test_create_order_success(self, mock_post, mock_generateAccessToken):
       
        mock_generateAccessToken.return_value = 'fake_access_token'
        
        mock_response = mock_post.return_value
        mock_response.json.return_value = {
            "id": "test_order_id",
            "status": "CREATED"
        }
        mock_response.status_code = 201
        
        
        productos = [{"nombre": "Producto Test", "precio": "5"}]
        response = create_order(productos)
        
       
        self.assertIsNotNone(response)
        self.assertEqual(response['id'], 'test_order_id')
        self.assertEqual(response['status'], 'CREATED')
        
       