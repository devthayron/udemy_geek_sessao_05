from django.test import TestCase
from core.forms import ContatoForm

class ContatoFormTestCase(TestCase):

    def setUp(self):
        self.nome = 'Thayron'
        self.email = 'devthayron@gmail.com'
        self.assunto = 'teste de email'
        self.mensagem = 'testando o envio do email'

        self.dados = {
            'nome': self.nome,
            'email': self.email,
            'assunto': self.assunto,
            'mensagem': self.mensagem,
        }

        self.form = ContatoForm(data=self.dados)    #ContatoForm(request.POST)

    def test_send_email(self):
        form1 = ContatoForm(data=self.dados)
        form1.is_valid()
        result1 = form1.send_email()

        form2 = ContatoForm(data=self.dados)
        form2.is_valid()
        result2 = form2.send_email()

        self.assertEqual(result1,result2)


