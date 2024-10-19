from django.test import TestCase
from .models import Produto

class ProdutoModelTest(TestCase):

    def setUp(self):
        # Criando um produto para usar nos testes
        self.produto = Produto.objects.create(
            nome="Produto Teste",
            preco=99.99,
            estoque=10
        )

    def test_produto_creation(self):
        # Verifica se o produto foi criado corretamente
        produto = self.produto
        self.assertEqual(produto.nome, "Produto Teste")
        self.assertEqual(produto.preco, 99.99)
        self.assertEqual(produto.estoque, 10)

    def test_produto_str(self):
        # Verifica se o método __str__ do produto está retornando o nome corretamente
        produto = self.produto
        self.assertEqual(str(produto), "Produto Teste")
