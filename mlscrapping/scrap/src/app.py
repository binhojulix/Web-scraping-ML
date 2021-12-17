from produtoBuilder import ProdutoBuilder



if __name__ == "__main__":
    produtoBuilder = ProdutoBuilder()
    produtoBuilder.com_titulo("produto ")
    produto = produtoBuilder.build()
    print(produto.preco)