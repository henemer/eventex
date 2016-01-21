
from django.core import mail
from django.test import TestCase


class SubsribePostValid(TestCase):
    def setUp(self):
        data= dict(name ='Emerson Henning', cpf='12345678901',
                        email='sisserv@sisserv.com.br', phone = '41-9650-9391')
        self.client.post('/inscricao/',data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'emerson@henning.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['emerson@henning.com.br','sisserv@sisserv.com.br']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Emerson Henning',
            '12345678901',
            'sisserv@sisserv.com.br',
            '41-9650-9391'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
