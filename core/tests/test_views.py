from django.test import TestCase,Client
from django.urls import reverse_lazy

class IndexViewTestCase(TestCase):
    
    def setUp(self):
        self.dados = {
            'nome': 'Thayron',
            'email': 'devthayron@gmail.com',
            'assunto': 'teste de email',
            'mensagem': 'testando o envio do email',
        }
        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Thayron',
            'mensagem': 'dados incompleto para dar erro',
        }
        request = self.client.post(reverse_lazy('index'), data=dados)
        self.assertEqual(request.status_code, 200)


