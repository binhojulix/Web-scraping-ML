from produto import Produto

class ProdutoBuilder(object):
    
    def __init__(self):
        self.reviews_amount = None
        self.cores_disponiveis = None
        self.frete = None
        self.titulo = None
        self.preco = None

    def com_reviews_amount(self, reviews_amount):
        self.reviews_amount = reviews_amount
        return self
    
    def com_cores_disponiveis(self, cor):
        self.cores_disponiveis = cor
        return self
    
    def com_frete(self, frete):
        self.frete = frete
        return self
    
    def com_titulo(self, titulo):
        self.titulo = titulo
        return self
    
    def com_preco(self, preco):
        self.preco = preco
        return self
    
    def build(self):
        if(self.titulo is None):
            raise Exception('Titulo deve ser preenchido')
        return Produto("0", "0", "0", "0", 200)
     